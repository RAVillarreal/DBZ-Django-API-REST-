from django.urls import path
from .views import *

app_name = 'dbzapi'

urlpatterns = [
    path('', CharacterList.as_view(), name='character_list'),
    path('character/<int:pk>/', CharacterDetail.as_view(), name='character_detail'),
    path('race/<int:pk>/', RaceDetail.as_view(), name='race_detail'),
    path('planet/<int:pk>/', PlanetDetail.as_view(), name='planet_detail'),
    path('technique/<int:pk>/', TechniqueDetail.as_view(), name='technique_detail'),
    path('location/<int:pk>/', LocationDetail.as_view(), name='location_detail'),
]