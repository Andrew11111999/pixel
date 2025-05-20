from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('mailings/', include('mailings.urls')),
    path('mldata/', include('mldata.urls')),
    path('pricing/', include('pricing.urls')),
    path('media/', include('media.urls')),
    path('games/', include('games.urls')),
    path('cases/', include('cases.urls')),
]
