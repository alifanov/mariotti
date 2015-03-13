from django.conf.urls import patterns, include, url
from app.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', TemplateView.as_view(template_name='empty.html'), name='home'),
    url(r'^contacts/$', ContactsView.as_view(), name='contacts'),
    url(r'^contacts/apply/$', ContactsApplyAjaxView.as_view(), name='contacts-apply'),
    url(r'^$', HomeView.as_view(), name='home-1'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^service/(?P<slug>[-\w]+)/$', ServiceDetail.as_view(), name='service'),
    url(r'^news/$', NewsList.as_view(), name='news'),
    url(r'^news/(?P<slug>[-\w]+)/$', NewsDetail.as_view(), name='news-item'),
    url(r'^portfolio/$', PortfolioList.as_view(), name='portfolio'),
    url(r'^portfolio/(?P<slug>[-\w]+)/$', PortfolioDetail.as_view(), name='portfolio-item'),
    url(r'^sitemap\.xml$', SitemapView.as_view(), name='sitemap'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
