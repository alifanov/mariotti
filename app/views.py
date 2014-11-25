from django.shortcuts import render
from app.models import *
from django.views.generic import ListView, DetailView, TemplateView
# Create your views here.

class GeneralMixin(object):
    def get_context_data(self, **kwargs):
        ctx = super(GeneralMixin, self).get_context_data(**kwargs)
        ctx['services'] = NewsItem.objects.order_by('-date')
        return ctx

class NewsList(ListView):
    model = NewsItem
    template_name = 'news-list.html'
    context_object_name = 'news'

class NewsDetail(DetailView):
    model = NewsItem
    template_name = 'news-item.html'
    context_object_name = 'n'

class ServiceDetail(DetailView):
    model = ServiceItem
    template_name = 'service.html'
    context_object_name = 'service'