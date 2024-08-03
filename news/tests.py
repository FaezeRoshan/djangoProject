
from django.test import TestCase
from .models import New, Tag

class NewsTestCase(TestCase):
    def setUp(self):
        tag1 = Tag.objects.create(tag="tag1")
        tag2 = Tag.objects.create(tag="tag2")
        news = New.objects.create(title="News title", text="News text", source="Source name")
        news.tags.set([tag1, tag2])

    def test_news_creation(self):
        news = New.objects.get(title="News title")
        self.assertEqual(news.text, "News text")
        self.assertEqual(news.source, "Source name")
        self.assertEqual(news.tags.count(), 2)
