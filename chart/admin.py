from django.contrib import admin
from chatbot.models import ChatModel


@admin.register(ChatModel)
class ChatModelAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    search_fields = ['question']
    list_filter = ['question']
