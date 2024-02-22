"""URL configuration for app project"""

from main import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("about/", views.about, name="about"),
]
