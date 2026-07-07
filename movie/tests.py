from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movie, Review, Watchlist
from django.urls import reverse

class CineWaveTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.movie = Movie.objects.create(
            title='Inception',
            description='A thief who steals corporate secrets...',
            url='https://example.com/inception'
        )
        
    def test_homepage_loading(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Inception')

    def test_movie_detail_view(self):
        response = self.client.get(reverse('detail', kwargs={'movie_id': self.movie.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Inception')
        self.assertContains(response, 'No reviews yet')

    def test_review_creation_with_rating(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(
            reverse('createreview', kwargs={'movie_id': self.movie.id}),
            {'myreview': 'Amazing masterpiece!', 'rating': '5'}
        )
        self.assertRedirects(response, reverse('detail', kwargs={'movie_id': self.movie.id}))
        
        review = Review.objects.get(movie=self.movie, user=self.user)
        self.assertEqual(review.text, 'Amazing masterpiece!')
        self.assertEqual(review.rating, 5)
        
        response = self.client.get(reverse('detail', kwargs={'movie_id': self.movie.id}))
        self.assertContains(response, '5.0')
        self.assertContains(response, 'Amazing masterpiece!')

    def test_watchlist_toggling(self):
        self.client.login(username='testuser', password='password123')
        
        response = self.client.get(reverse('toggle_watchlist', kwargs={'movie_id': self.movie.id}))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Watchlist.objects.filter(user=self.user, movie=self.movie).exists())
        
        response = self.client.get(reverse('watchlist'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Inception')
        
        self.client.get(reverse('toggle_watchlist', kwargs={'movie_id': self.movie.id}))
        self.assertFalse(Watchlist.objects.filter(user=self.user, movie=self.movie).exists())
