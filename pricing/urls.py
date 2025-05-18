from django.urls import path
from . import views

urlpatterns = [
    path('api/pricing/', views.pricing_list_api, name='pricing_list_api'),
    path('api/pricing/<int:pk>/', views.pricing_detail_api, name='pricing_detail_api'),
]

