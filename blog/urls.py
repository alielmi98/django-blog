from django.contrib import admin
from django.urls import path
from blog.views import blog_index_view,blog_single_view
app_name='blog'
urlpatterns = [
    path('',blog_index_view,name='index'),
    path('single',blog_single_view,name='single'),
]
