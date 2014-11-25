from django.contrib import admin
from app.models import *
# Register your models here.

class NewsItemImageInline(admin.TabularInline):
    model = NewsImage

class NewsItemAdmin(admin.ModelAdmin):
    inlines = [NewsItemImageInline,]


class ServiceItemImageInline(admin.TabularInline):
    model = ServiceItemImage

class ServiceItemAdmin(admin.ModelAdmin):
    inlines = [ServiceItemImageInline,]


class PortfolioItemImageInline(admin.TabularInline):
    model = PortfolioItemImage

class PortfolioItemAdmin(admin.ModelAdmin):
    inlines = [PortfolioItemImageInline,]

admin.site.register(PortfolioItem, PortfolioItemAdmin)
admin.site.register(ServiceItem, ServiceItemAdmin)
admin.site.register(NewsItem, NewsItemAdmin)