from django.shortcuts import render

# Create your views here.

class GeneralMixin(object):
    def get_context_data(self, **kwargs):
        ctx = super(GeneralMixin, self).get_context_data(**kwargs)
        ctx['services']
        return ctx
