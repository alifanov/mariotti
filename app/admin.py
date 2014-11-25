from django.contrib import admin
from app.models import *
# Register your models here.

class NewsItemImageInline(admin.TabularInline):
    model = NewsImage

class NewsItemAdmin(admin.ModelAdmin):
    inlines = [NewsItemImageInline,]

admin.site.register(PortfolioItem)
admin.site.register(ServiceItem)
admin.site.register(NewsItem, NewsItemAdmin)