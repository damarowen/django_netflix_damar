from django.urls import path

from netflix.views import Home, ProfileCreate, ProfileList, ShowMovie, ShowMovieDetail, Watch

app_name = 'netflix'

urlpatterns = [
    path('', Home.as_view()),
    path('profile/', ProfileList.as_view(), name='profile_list'),
    path('profile/create/', ProfileCreate.as_view(), name='profile_create'),
    path('watch/<str:profile_id>/',Watch.as_view(),name='watch'),
    path('movie/detail/<str:movie_id>/',ShowMovieDetail.as_view(),name='show_det'),
     path('movie/play/<str:movie_id>/',ShowMovie.as_view(),name='play')
]
