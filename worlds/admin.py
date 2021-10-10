from django.contrib import admin

from .models import Character, Episode, Medium, Series, UnitOfFiction, Universe

# Register your models here.
admin.site.register(Character)
admin.site.register(Episode)
admin.site.register(Medium)
admin.site.register(Series)
admin.site.register(UnitOfFiction)
admin.site.register(Universe)
