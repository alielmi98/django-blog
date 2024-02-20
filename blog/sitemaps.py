from django.contrib.sitemaps import Sitemap
from blog.models import Post
from django.utils import timezone
from django.urls import reverse


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        now = timezone.now()
        return Post.objects.filter(status=1).filter(published_date__lte = now)

    def lastmod(self, obj):
        return obj.published_date
    
    def location(self,item):
        return reverse('blog:single', kwargs={'pid': item.id})

