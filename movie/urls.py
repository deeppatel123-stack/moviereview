from django.urls import path
from movie import views as movieViews

urlpatterns = [
    path('<int:movie_id>',movieViews.detail,name='detail'),
    path('<int:movie_id>/create',movieViews.createreview,name='createreview'),
    path('review/<int:review_id>',movieViews.updatereview,name='updatereview'),
    path('review/<int:review_id>/delete',movieViews.deletereview,name='deletereview'),
    path('watchlist/', movieViews.watchlist, name='watchlist'),
    path('watchlist/toggle/<int:movie_id>/', movieViews.toggle_watchlist, name='toggle_watchlist'),
]