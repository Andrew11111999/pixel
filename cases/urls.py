from django.urls import path
from . import views

urlpatterns = [
    path('api/case_list/', views.case_list_api, name='case_list_api'),
    path('api/case_detail/<int:pk>/', views.case_detail_api, name='case_detail_api'),
]
