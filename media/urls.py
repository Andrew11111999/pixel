from django.urls import path
from . import views

urlpatterns = [
    path('api/media/', views.media_list_api, name='media_list_api'),
    path('api/media/<int:pk>/', views.media_detail_api, name='media_detail_api'),
]
