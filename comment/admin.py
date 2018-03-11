from django.contrib import admin
from .models import Comment

# Register your models here.

class CommnetAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'created_time',
        'text',
        'post',
    ]

admin.site.register(Comment, CommnetAdmin)