

from django.urls import path

from . import views

urlpatterns = [
    path('ctc/', views.getCTC),
    path('cts/', views.getCTS),
    path('ttc/', views.getTTC),
    path('tts/', views.getTTS),
    path('url/', views.getURL),
]