# music_analysis/urls.py
from django.urls import path
from .views import home,recommend_songs,new_page

urlpatterns = [
    path('', home, name='home'),
    path('recommend/', recommend_songs, name='recommend_songs'),
]
