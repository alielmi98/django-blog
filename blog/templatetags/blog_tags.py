from django import template
from blog.models import Post,Category
from django.utils import timezone

register=template.Library()

@register.inclusion_tag("blog/blog_lastes_post.html")
def lastespost(arg=3):
    now=timezone.now()
    posts=Post.objects.filter(status=1).filter(published_date__lte = now).order_by('-published_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag("blog/blog_post_categories.html")
def postcategories():
    now=timezone.now()
    posts=Post.objects.filter(status=1).filter(published_date__lte = now)
    categories=Category.objects.all()
    cat_dic={}
    for name in categories:
        cat_dic[name]=posts.filter(category=name).count()
    return {'categories':cat_dic}

