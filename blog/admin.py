from django.contrib import admin
from .models import Category,Post,Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'title',
        'created_time',
        'modified_time',
        'author'
    ]

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
