from django.contrib import admin
from django.contrib.admin import BooleanFieldListFilter
from django.utils.translation import ugettext_lazy as _
from blog.models import Article, ArticleImage

class ArticleImage_Inline(admin.TabularInline):
    model = ArticleImage
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",),
    }

    list_per_page = 25

    list_display = (
        '__str__',
        'is_active',
        'date',
        'meta_description',
        'meta_keywords',
    )

    list_filter = (
        ('is_active', BooleanFieldListFilter),
    )

    search_fields = ['slug', 'name', 'date',]
    inlines = [ ArticleImage_Inline, ]

admin.site.register(Article, ArticleAdmin)
