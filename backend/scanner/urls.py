from .views import ping_scan_view, detailed_scan_view

from django.urls import path

urlpatterns = [
    path('ping-scan/', ping_scan_view, name='ping-scan'),
    path('detailed-scan/', detailed_scan_view, name='detailed-scan'),
]