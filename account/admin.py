from django.contrib import admin
from .models import User


@admin.register(User)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'email', 'profile_image')
    search_fields = ['username']
    list_filter = ['username']