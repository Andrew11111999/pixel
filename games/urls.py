from django.urls import path
from . import views

urlpatterns = [
    path('api/games_list/', views.game_list_api, name='game_list_api'),  # API: список всех игр
    path('api/games_detail/<int:pk>/', views.game_detail_api, name='game_detail_api'),  # API: детали конкретной игры
]
