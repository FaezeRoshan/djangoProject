from django.db import models

# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=50, unique=True)

class New(models.Model):
    title = models.CharField(max_length=200)
    text =models.TextField()
    tags = models.ManyToManyField(Tag)
    source = models.CharField(max_length=200)


