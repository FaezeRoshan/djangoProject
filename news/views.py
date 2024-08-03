from django.shortcuts import render



from rest_framework import viewsets, filters
from .models import New,Tag
from .serializers import NewSerializer

class NewViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['tags__tag']
    #/url/news/?search=tag_name


