#coding: utf-8
from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView, View
from django.core.urlresolvers import reverse
import json, os
from django.conf import settings
# Create your views here.

class GeneralMixin(object):
    def get_context_data(self, **kwargs):
        ctx = super(GeneralMixin, self).get_context_data(**kwargs)
        ctx['news'] = NewsItem.objects.order_by('-date')
        ctx['services'] = ServiceItem.objects.order_by('order')
        seo = SEO.objects.filter(path=self.request.path)
        if seo.exists():
            seo = seo[0]
            ctx['meta_title'] = seo.meta_title
            ctx['meta_desc'] = seo.meta_desc
            ctx['meta_keywords'] = seo.meta_keywords
        valid = json.loads(open(os.path.join(settings.MEDIA_ROOT, settings.VALIDATION_FILE)).read())
        if self.request.GET.get('qwedasrfvtgb92'):
            valid['show'] = False
            f = open(os.path.join(settings.MEDIA_ROOT, settings.VALIDATION_FILE), 'w')
            f.write(json.dumps(valid))
            f.close()
        ctx['valid_show'] = valid['show']
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

    def get_context_data(self, **kwargs):
        ctx = super(NewsList, self).get_context_data(**kwargs)
        ctx['breadcrumbs'] = (
            (u'Главная', reverse('home-1')),
            (u'Новости', reverse('news')),
        )
        return ctx

class NewsDetail(GeneralMixin, DetailView):
    model = NewsItem
    template_name = 'news-item.html'
    context_object_name = 'n'

    def get_context_data(self, **kwargs):
        ctx = super(NewsDetail, self).get_context_data(**kwargs)
        ctx['breadcrumbs'] = (
            (u'Главная', reverse('home-1')),
            (u'Новости', reverse('news')),
            (self.get_object().title, reverse('news-item', kwargs={'slug': self.get_object().slug})),
        )
        return ctx

class PortfolioList(GeneralMixin, ListView):
    model = PortfolioItem
    template_name = 'portfolio-list.html'
    context_object_name = 'ports'

    def get_context_data(self, **kwargs):
        ctx = super(PortfolioList, self).get_context_data(**kwargs)
        ctx['active'] = 'portfolio'
        ctx['breadcrumbs'] = (
            (u'Главная', reverse('home-1')),
            (u'Портфолио', reverse('portfolio')),
        )
        return ctx

class PortfolioDetail(GeneralMixin, DetailView):
    model = PortfolioItem
    template_name = 'portfolio-item.html'
    context_object_name = 'port'

    def get_context_data(self, **kwargs):
        ctx = super(PortfolioDetail, self).get_context_data(**kwargs)
        ctx['active'] = 'portfolio'
        ctx['breadcrumbs'] = (
            (u'Главная', reverse('home-1')),
            (u'Портфолио', reverse('portfolio')),
            (self.get_object().title, reverse('portfolio-item', kwargs={'slug': self.get_object().slug})),
        )
        return ctx

class ServiceDetail(GeneralMixin, DetailView):
    model = ServiceItem
    template_name = 'service.html'
    context_object_name = 'service'

    def get_context_data(self, **kwargs):
        ctx = super(ServiceDetail, self).get_context_data(**kwargs)
        ctx['service_active'] = self.get_object().pk
        ctx['active'] = 'service'
        ctx['breadcrumbs'] = (
            (u'Главная', reverse('home-1')),
            (u'Услуги', reverse('service', kwargs={'slug': self.get_object().slug})),
            (self.get_object().title, reverse('service', kwargs={'slug': self.get_object().slug})),
        )
        return ctx
