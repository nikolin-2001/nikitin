from django.urls import re_path, path
from .views import komplekt_list, komplekt_detail, komplekt_list_published

urlpatterns = [
    re_path(r'^api/tutorials$', komplekt_list),
    re_path(r'^api/tutorials/(?P<pk>[0-9]+)$', komplekt_detail),
    re_path(r'^api/tutorials/published$', komplekt_list_published)
]
