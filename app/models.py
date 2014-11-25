#coding: utf-8
from django.db import models

# Create your models here.


class NewsItem(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'Title')
    date = models.DateField(auto_now_add=True, verbose_name=u'Date', editable=True)
    short_desc = models.TextField(blank=True, null=True, verbose_name=u'Short desc')
    text = models.TextField(verbose_name=u'Text')

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

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = u'Services'
        verbose_name = u'Service'

# class ServiceItemImage(models.Model):
#     image = models.ImageField(upload_to=u'uploads/', verbose_name=u'Image')
#     service = models.ForeignKey(verbose_name=u'Service', related_name='images')
#
#     def __unicode__(self):
#         return self.pk
#
#     class Meta:
#         verbose_name = u'Service Image'
#         verbose_name_plural = u'Service Images'