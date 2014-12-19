from django.contrib import admin
from app.models import *
from redactor.widgets import AdminRedactorEditor
# Register your models here.

from django import forms

class ServiceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget = AdminRedactorEditor()

class NewsItemImageInline(admin.TabularInline):
    model = NewsImage

class NewsItemAdmin(admin.ModelAdmin):
    inlines = [NewsItemImageInline,]
    prepopulated_fields = {"slug": ("title",)}


class ServiceItemImageInline(admin.TabularInline):
    model = ServiceItemImage

class ServiceItemAdmin(admin.ModelAdmin):
    inlines = [ServiceItemImageInline,]
    prepopulated_fields = {"slug": ("title",)}
    form = ServiceForm

class PortfolioItemImageInline(admin.TabularInline):
    model = PortfolioItemImage

class PortfolioItemAdmin(admin.ModelAdmin):
    inlines = [PortfolioItemImageInline,]
    prepopulated_fields = {"slug": ("title",)}

class PageItemImageInline(admin.TabularInline):
    model = PageImage

class PageItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PageItemForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget = AdminRedactorEditor()

class PageItemAdmin(admin.ModelAdmin):
    inlines = [PageItemImageInline,]
    prepopulated_fields = {"slug": ("title",)}
    form = PageItemForm


admin.site.register(PortfolioItem, PortfolioItemAdmin)
admin.site.register(ServiceItem, ServiceItemAdmin)
admin.site.register(NewsItem, NewsItemAdmin)
admin.site.register(PageItem, PageItemAdmin)
admin.site.register(ContactFormApply)