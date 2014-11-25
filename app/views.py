from django.shortcuts import render
from app.models import *
from django.views.generic import ListView, DetailView, TemplateView
# Create your views here.

class GeneralMixin(object):
    def get_context_data(self, **kwargs):
        ctx = super(GeneralMixin, self).get_context_data(**kwargs)
        ctx['news'] = NewsItem.objects.order_by('-date')
        ctx['services'] = ServiceItem.objects.order_by('order')
        return ctx

class HomeView(GeneralMixin, TemplateView):
    template_name = 'home.html'

class AboutView(GeneralMixin, TemplateView):
    template_name = 'about.html'

class NewsList(GeneralMixin, ListView):
    model = NewsItem
    template_name = 'news-list.html'
    context_object_name = 'news'

class NewsDetail(GeneralMixin, DetailView):
    model = NewsItem
    template_name = 'news-item.html'
    context_object_name = 'n'

class PortfolioList(GeneralMixin, ListView):
    model = PortfolioItem
    template_name = 'portfolio-list.html'
    context_object_name = 'ports'

class PortfolioDetail(GeneralMixin, DetailView):
    model = PortfolioItem
    template_name = 'portfolio-item.html'
    context_object_name = 'port'

class ServiceDetail(GeneralMixin, DetailView):
    model = ServiceItem
    template_name = 'service.html'
    context_object_name = 'service'

    def get_context_data(self, **kwargs):
        ctx = super(ServiceDetail, self).get_context_data(**kwargs)
        ctx['service_active'] = self.get_object().pk
        return ctx
