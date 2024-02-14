from django.contrib import admin
from .models import Post,Category
# Register your models here.

@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["title","counted_views", "status", "published_date","created_date"]
    date_hierarchy = 'created_date'
    list_filter = ('status',)
    search_fields = ['title','content']

@admin.register(Category)
class AuthorAdmin(admin.ModelAdmin):
    pass
