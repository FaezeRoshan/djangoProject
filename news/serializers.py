

from rest_framework import serializers
from .models import New, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'tag']

class NewSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = New
        fields = ['id', 'title', 'tags', 'source']
