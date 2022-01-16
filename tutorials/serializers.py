from rest_framework import serializers
from tutorials.models import Komplekt

class KomplektSerializer(serializers.ModelSerializer):
    class Meta:
        model = Komplekt
        fields = ('id',
                  'name',
                  'description',
                  'price',
                  'published',
                  'year')