import warnings
from datetime import date
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible
from sorl.thumbnail import ImageField
from tinymce import models as tinymce_models

@python_2_unicode_compatible
class Article(models.Model):

    name = models.CharField(
            _("Full Name"),
            max_length=255,
            help_text=_("Article Name"))

    slug = models.SlugField(
            _("Slug Field"),
            unique=True,
            max_length=255,
            help_text=_("Required to construct URL. Generated from name."))

    date = models.DateField(
            _("Relevant Date"),
            default=date.today,
            help_text=_("Date you wrote the story."))
            
    content = tinymce_models.HTMLField(
            blank=True,
            help_text=_("The full article you wanted to write."))

    is_active = models.BooleanField(
            _("Active"),
            default=True,
            help_text=_("Usefull for temporarily hiding an article."))

    meta_description = models.CharField(
            _("Meta Description"),
            max_length=300,
            blank=True,
            help_text=_("300 Character description of the article."))

    meta_keywords = models.CharField(
            _("Meta Keywords"),
            max_length=300,
            blank=True,
            help_text=_("List of comma seperated words related to the article, max=300 chars"))

    def __str__(self):
        return '%s - %s' % (self.name, self.date)

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'slug':self.slug})
        
    class Meta:
        app_label = 'blog'
        ordering = ['date','name']
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

@python_2_unicode_compatible
class ArticleImage(models.Model):
    article = models.ForeignKey('Article')
    image = models.ImageField(upload_to="ArticleImages/", blank=True, null=True)
    caption = models.CharField(_("Optional caption"), max_length=100, null=True, blank=True)
    sort = models.IntegerField(_("Sort Order"), default=0)
    
    def __str__(self):
        if self.caption:
            return '%s...' % (self.caption[:47])
        else:
            return '%s' % (self.article)

    class Meta:
        app_label = 'blog'
        ordering = ['sort']
        verbose_name = _('Article Image')
        verbose_name_plural = _('Article Images')


