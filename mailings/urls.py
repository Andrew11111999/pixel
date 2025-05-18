from django.urls import path, include
from . import views

urlpatterns = [
    path('api/add_to_common_list/', views.add_email_to_common_mailchimp_list_view, name='add_to_common_list_api'),
    path('api/add_to_case_list/<int:pk>/', views.add_email_to_case_mailchimp_list_view, name='add_to_case_list_api'),
]

