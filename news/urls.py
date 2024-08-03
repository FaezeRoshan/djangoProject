# news/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewViewSet
from .collectnews import addnews

router = DefaultRouter()
router.register(r'news', NewViewSet, basename='new')

urlpatterns = [
    path('', include(router.urls)),


]
