from django.urls import re_path
from .views import komplekt_list, komplekt_detail, komplekt_list_published, music_detail, music_list, music_list_published

urlpatterns = [
    re_path(r'^api/tutorials$', komplekt_list),
    re_path(r'^api/tutoria  ls/(?P<pk>[0-9]+)$', komplekt_detail),
    re_path(r'^api/tutorials/published$', komplekt_list_published),
    re_path(r'^api/music$', music_list),
    re_path(r'^api/music/(?P<pk>[0-9]+)$', music_detail),
    re_path(r'^api/music/published$', music_list_published),
]
