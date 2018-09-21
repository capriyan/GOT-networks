from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home, name='app-home'),
    path('about/', views.about, name='app-about'),
    path('characters/', views.all_characters, name='app-characters'),
    path('occurrences/', views.all_occurrences, name='app-occurrences'),
]