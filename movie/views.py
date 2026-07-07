from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie,Review,Watchlist
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required                   
from django.db.models import Avg

# Create your views here.
def home(request):
    searchTerm = request.GET.get('searchMovie')
    sort_by = request.GET.get('sort_by', 'title_asc')
    
    # Annotate movies with average rating
    movies = Movie.objects.annotate(average_rating=Avg('review__rating'))
    
    if searchTerm:
        movies = movies.filter(title__icontains=searchTerm)
        
    if sort_by == 'title_asc':
        movies = movies.order_by('title')
    elif sort_by == 'title_desc':
        movies = movies.order_by('-title')
    elif sort_by == 'rating_desc':
        movies = movies.order_by('-average_rating')
        
    return render(request, 'home.html', {
        'searchTerm': searchTerm,
        'movies': movies,
        'sort_by': sort_by,
    })

def about(request):
    return render(request,'about.html')

def signup(request):
    email = request.GET.get('email')
    return render(request,'signup.html',{'email':email})


def detail(request,movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    reviews = Review.objects.filter(movie=movie).order_by('-date')
    
    # Calculate average rating
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    if avg_rating is not None:
        avg_rating = round(avg_rating, 1)
        
    # Check if in watchlist
    in_watchlist = False
    if request.user.is_authenticated:
        in_watchlist = Watchlist.objects.filter(user=request.user, movie=movie).exists()
        
    return render(request, 'detail.html', {
        'movie': movie,
        'reviews': reviews,
        'avg_rating': avg_rating,
        'in_watchlist': in_watchlist,
    })

@login_required
def createreview(request,movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    if request.method == 'GET':
        return render(request,'createreview.html',{'movie':movie})
    else:
        try:
            myreview = request.POST.get('myreview')
            rating = request.POST.get('rating', 5)
            try:
                rating = int(rating)
            except (ValueError, TypeError):
                rating = 5
                
            newReview = Review()
            newReview.user = request.user
            newReview.movie = movie
            newReview.text = myreview
            newReview.rating = rating
            newReview.save()
            return redirect('detail',newReview.movie.id)
        except ValueError:
            return render(request,'createreview.html',
                          {'error':'bad data passed in'})
        
@login_required
def updatereview(request,review_id):
    review = get_object_or_404(Review,pk=review_id,user=request.user)
    if request.method == 'GET':
        return render(request,'updatereview.html',{'review':review})
    else:
        try:
            review.text = request.POST.get('myreview')
            rating = request.POST.get('rating')
            if rating:
                try:
                    review.rating = int(rating)
                except ValueError:
                    pass
            review.save()
            return redirect('detail',review.movie.id)
        except ValueError:
            return render(request,'updatereview.html',
                          {'review':review,'error':'Bad Data passed in'})
        
@login_required
def deletereview(request,review_id):
    review = get_object_or_404(Review,pk=review_id,user=request.user)
    movie_id = review.movie.id
    review.delete()
    return redirect('detail',movie_id)

@login_required
def toggle_watchlist(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    watchlist_item = Watchlist.objects.filter(user=request.user, movie=movie)
    if watchlist_item.exists():
        watchlist_item.delete()
    else:
        Watchlist.objects.create(user=request.user, movie=movie)
    
    referer = request.META.get('HTTP_REFERER')
    if referer:
        return redirect(referer)
    return redirect('detail', movie.id)

@login_required
def watchlist(request):
    items = Watchlist.objects.filter(user=request.user).select_related('movie')
    movies = []
    for item in items:
        # Calculate rating for each watchlisted movie
        avg = Review.objects.filter(movie=item.movie).aggregate(Avg('rating'))['rating__avg']
        item.movie.average_rating = round(avg, 1) if avg is not None else None
        movies.append(item.movie)
        
    return render(request, 'watchlist.html', {'movies': movies})

    