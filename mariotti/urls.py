from django.conf.urls import patterns, include, url
from app.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='empty.html'), name='home'),
    url(r'^contacts/$', TemplateView.as_view(template_name='contacts.html'), name='contacts'),
    url(r'^home/$', TemplateView.as_view(template_name='home.html'), name='home-1'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^service/(?P<pk>\d+)/$', ServiceDetail.as_view(), name='service'),
    url(r'^news/$', NewsList.as_view(), name='news'),
    url(r'^portfolio-all/$', TemplateView.as_view(template_name='portfolio-list.html'), name='portfolio-all'),
    url(r'^news/(?P<pk>\d+)/$', NewsDetail.as_view(), name='news-item'),
    url(r'^portfolio-item/$', TemplateView.as_view(template_name='portfolio-item.html'), name='portfolio-item'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
