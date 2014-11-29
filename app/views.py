from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView, View
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

    def get_context_data(self, **kwargs):
        ctx = super(AboutView, self).get_context_data(**kwargs)
        ctx['page'] = PageItem.objects.get(slug='about')
        ctx['active'] = 'about'
        return ctx

class ContactsView(GeneralMixin, TemplateView):
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        ctx = super(ContactsView, self).get_context_data(**kwargs)
        ctx['form'] = ContactPageForm()
        ctx['active'] = 'contacts'
        return ctx

class ContactsApplyAjaxView(View):
    def post(self, request, *args, **kwargs):
        form = ContactPageForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse('OK')

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

    def get_context_data(self, **kwargs):
        ctx = super(PortfolioList, self).get_context_data(**kwargs)
        ctx['active'] = 'portfolio'
        return ctx

class PortfolioDetail(GeneralMixin, DetailView):
    model = PortfolioItem
    template_name = 'portfolio-item.html'
    context_object_name = 'port'

    def get_context_data(self, **kwargs):
        ctx = super(PortfolioDetail, self).get_context_data(**kwargs)
        ctx['active'] = 'portfolio'
        return ctx

class ServiceDetail(GeneralMixin, DetailView):
    model = ServiceItem
    template_name = 'service.html'
    context_object_name = 'service'

    def get_context_data(self, **kwargs):
        ctx = super(ServiceDetail, self).get_context_data(**kwargs)
        ctx['service_active'] = self.get_object().pk
        ctx['active'] = 'service'
        return ctx
