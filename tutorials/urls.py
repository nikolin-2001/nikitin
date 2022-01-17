from django.urls import re_path
from .views import komplekt_list, komplekt_detail, komplekt_list_published, music_list, music_detail, music_list_published

urlpatterns = [
    re_path(r'^api/tutorials$', komplekt_list),
    re_path(r'^api/tutorials/(?P<pk>[0-9]+)$', komplekt_detail),
    re_path(r'^api/tutorials/published$', komplekt_list_published),
    re_path(r'^api/musics$', music_list),
    re_path(r'^api/musics/(?P<pk>[0-9]+)$', music_detail),
    re_path(r'^api/musics/published$', music_list_published),
]
