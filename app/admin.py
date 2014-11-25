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

admin.site.register(PortfolioItem)
admin.site.register(ServiceItem, ServiceItemAdmin)
admin.site.register(NewsItem, NewsItemAdmin)