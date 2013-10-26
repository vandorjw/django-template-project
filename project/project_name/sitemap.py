from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from blog.models import Article


class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Article.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.date


class HardCodedSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['contactpage', 'homepage']

    def location(self, item):
        return reverse(item)

