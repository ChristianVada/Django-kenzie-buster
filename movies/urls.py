from django.urls import path
from movies.views import *

urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<int:movie_id>/", MovieDetailsView.as_view()),
    path("movies/<int:movie_id>/orders/", MovieOrderDetailsView.as_view()),
]
