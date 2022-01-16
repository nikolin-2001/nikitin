from django.urls import re_path, path, include
from django.contrib import admin

urlpatterns = [
    re_path(r'^', include('tutorials.urls')),
    path('admin/', admin.site.urls),
]
