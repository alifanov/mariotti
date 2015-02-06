#coding: utf-8
from django.db import models

# Create your models here.

class SEO(models.Model):
    path = models.CharField(max_length=255, verbose_name=u'URL')
    meta_title = models.TextField(verbose_name=u'META title', blank=True, null=True)
    meta_desc = models.TextField(verbose_name=u'META description', blank=True, null=True)
    meta_keywords = models.TextField(verbose_name=u'META keywords', blank=True, null=True)

    def __unicode__(self):
        return self.path

    class Meta:
        verbose_name = u'SEO'
        verbose_name_plural = u'SEO'


class ContactFormApply(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'Created')
    name = models.CharField(max_length=255, verbose_name=u'Name')
    email = models.CharField(max_length=255, verbose_name=u'E-mail')
    text = models.TextField(blank=True, null=True, verbose_name=u'Text')

    def __unicode__(self):
        return u'{}: {}'.format(self.created.strftime('%H:%I %d.%m.%Y'), self.name)

    class Meta:
        verbose_name = u'Contact apply'
        verbose_name_plural = u'Contact applies'

class PageItem(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'Title')
    text = models.TextField(verbose_name=u'Text')
    slug = models.CharField(max_length=255, verbose_name=u'Slug')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = u'Pages'
        verbose_name = u'Page'

class PageImage(models.Model):
    image = models.ImageField(verbose_name=u'Image', upload_to=u'uploads/')
    page = models.ForeignKey(PageItem, related_name='images')

    def __unicode__(self):
        return self.pk

    class Meta:
        verbose_name = u'Page images'
        verbose_name_plural = u'Page image'


class NewsItem(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'Title')
    date = models.DateField(verbose_name=u'Date')
    short_desc = models.TextField(blank=True, null=True, verbose_name=u'Short desc')
    text = models.TextField(verbose_name=u'Text')
    slug = models.CharField(max_length=255, verbose_name=u'Slug')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = u'Новости'
        verbose_name = u'Новость'

class NewsImage(models.Model):
    image = models.ImageField(verbose_name=u'Image', upload_to=u'uploads/')
    news = models.ForeignKey(NewsItem, related_name='images')

    def __unicode__(self):
        return self.pk

    class Meta:
        verbose_name = u'News images'
        verbose_name_plural = u'News image'


class PortfolioItem(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'Title')
    short_desc = models.TextField(blank=True, null=True, verbose_name=u'Short desc')
    text = models.TextField(verbose_name=u'Text')
    date = models.DateField(verbose_name=u'Date')
    slug = models.CharField(max_length=255, verbose_name=u'Slug')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = u'Portfolio items'
        verbose_name = u'Portfolio item'

class PortfolioItemImage(models.Model):
    image = models.ImageField(upload_to=u'uploads/', verbose_name=u'Image')
    portfolio = models.ForeignKey(PortfolioItem, verbose_name=u'Portfolio item', related_name='images')

    def __unicode__(self):
        return self.pk

    class Meta:
        verbose_name = u'Portfolio item image'
        verbose_name_plural = u'Portfolio item images'

class ServiceItem(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'Title')
    short_desc = models.TextField(blank=True, null=True, verbose_name=u'Short desc')
    icon = models.ImageField(verbose_name=u'Icon', upload_to=u'uploads/')
    text = models.TextField(verbose_name=u'Text')
    order = models.IntegerField(default=0, verbose_name=u'Order')
    slug = models.CharField(max_length=255, verbose_name=u'Slug')

    def is_long(self):
        if self.title.count('<br/>') == 2:
            return True

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = u'Services'
        verbose_name = u'Service'

class ServiceItemImage(models.Model):
    image = models.ImageField(upload_to=u'uploads/', verbose_name=u'Image')
    service = models.ForeignKey(ServiceItem, verbose_name=u'Service', related_name='images')

    def __unicode__(self):
        return self.pk

    class Meta:
        verbose_name = u'Service Image'
        # verbose_name_plural = u'Service Images'