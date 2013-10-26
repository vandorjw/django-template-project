from django.conf.urls.defaults import url, patterns, include
from blog import views

urlpatterns = patterns("",
    url(
        regex=r"^$",
        view=views.ArticleListView.as_view(),
        name='article_list',
    ),
    url(
        regex=r"^(?P<slug>[-\w]+)/$",
        view=views.ArticleDetailView.as_view(),
        name="article_detail",
    ),
)
