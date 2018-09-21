from django.contrib import admin
from app.models import Character, CoOccur, Book

admin.site.register(Character)
admin.site.register(CoOccur)
admin.site.register(Book)