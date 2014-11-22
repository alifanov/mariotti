from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='empty.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^service/$', TemplateView.as_view(template_name='service.html'), name='service'),
    url(r'^news-all/$', TemplateView.as_view(template_name='news-list.html'), name='news-all'),
    url(r'^portfolio-all/$', TemplateView.as_view(template_name='portfolio-list.html'), name='portfolio-all'),
    url(r'^news-item/$', TemplateView.as_view(template_name='news-item.html'), name='news-item'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
