from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from pathlib import Path


urlpatterns = [
    path('', include("core.urls"))
]

if settings.ADMINSITE:
    urlpatterns.append(path('admin/', admin.site.urls))
