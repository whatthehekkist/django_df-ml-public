from django.contrib import admin
from .models import Movies


@admin.register(Movies)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_id', 'title', 'genre', 'movie_image')
    search_fields = ['movie_id']
    list_filter = ['title']
