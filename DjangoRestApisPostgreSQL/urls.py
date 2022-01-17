from django.urls import re_path, path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'api/', include('tutorials.urls')),
]
