from django.contrib import admin

# Register your models here.
from .models import New
from .models import Tag
admin.site.register(Tag)

admin.site.register(New)

