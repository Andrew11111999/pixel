from django.urls import path
from . import views

urlpatterns = [
    # GameGenreMLData API
    path('api/ml/genre/', views.ml_genre_list_api, name='ml_genre_list'),
    path('api/ml/genre/<int:pk>/', views.ml_genre_detail_api, name='ml_genre_detail'),

    # GameMood API
    path('api/ml/moods/', views.ml_moods_list_api, name='ml_moods_list'),
    path('api/ml/moods/<int:pk>/', views.ml_mood_detail_api, name='ml_mood_detail'),

    # GameSubgenreMLData API
    path('api/ml/subgenres/', views.ml_subgenre_list_api, name='ml_subgenre_list'),
    path('api/ml/subgenres/<int:pk>/', views.ml_subgenre_detail_api, name='ml_subgenre_detail'),

    # GamePlatformMLData API
    path('api/ml/platforms/', views.ml_platform_list_api, name='ml_platform_list'),
    path('api/ml/platforms/<int:pk>/', views.ml_platform_detail_api, name='ml_platform_detail'),
]
