from django.contrib import admin
from .models import ChatModel

@admin.register(ChatModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('email', 'created')
    list_filter = ('email', 'created', 'updated')
    search_fields = ('email', 'body')
