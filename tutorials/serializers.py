from rest_framework import serializers
from tutorials.models import Komplekt, Music


class KomplektSerializer(serializers.ModelSerializer):
    class Meta:
        model = Komplekt
        fields = ('id',
                  'name',
                  'description',
                  'price',
                  'published',
                  'year')


class MusicSerializer(serializers.ModelSerializer):
    model = Music
    fields = ('id',
        'name',
        'price',
        'descriptions')
