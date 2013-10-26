from django.views import generic
from blog.models import Article

class ArticleListView(generic.ListView):
    model = Article
    queryset = Article.objects.filter(is_active=True)

class ArticleDetailView(generic.DetailView):
    model = Article
    slug_field = 'slug'
