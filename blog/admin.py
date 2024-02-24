from django.contrib import admin
from .models import Post,Category
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

@admin.register(Post)
class AuthorAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ["title","counted_views", "status", "published_date","created_date"]
    date_hierarchy = 'created_date'
    list_filter = ('status',)
    search_fields = ['title','content']

@admin.register(Category)
class AuthorAdmin(admin.ModelAdmin):
    pass


