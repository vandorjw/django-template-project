from django.conf.urls import patterns, include, url
from django.contrib.sitemaps import Sitemap
from django.views.generic import TemplateView
from django.contrib import admin
from {{ project_name }}.views import HomePageView, ContactPageView, RobotPageView, HumanPageView
from {{ project_name }}.sitemap import BlogSitemap, HardCodedSitemap

admin.autodiscover()

sitemaps = {
    'blog': BlogSitemap,
    'hardcodedpages': HardCodedSitemap,
}

urlpatterns = patterns('',
    url(
        regex=r"^$",
        view=HomePageView.as_view(),
        name="homepage",
    ),
    url(
        regex=r"^contact/$",
        view=ContactPageView.as_view(),
        name="contactpage",
    ),
    url(
        regex=r"^robots\.txt$",
        view=RobotPageView.as_view(),
        name="robots",
    ),
    url(
        regex=r"^humans\.txt$",
        view=HumanPageView.as_view(),
        name="humans",
    ),

    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url("^blog/", include('blog.urls', namespace='blog', app_name='blog')),
)
