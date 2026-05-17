from django.urls import path
from . import views

urlpatterns = [
    # Główny interfejs pod adresem /hello/
    path('', views.interactive_video_view, name='powitanie'),
    
    # Endpoint API pod adresem /hello/api/story/
    path('api/story/', views.api_get_story, name='api_story'),
]