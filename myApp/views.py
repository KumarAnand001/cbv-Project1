from typing import Any
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

# Create your views here.
class HelloWorldView(View):

    def get(self, request):

        return HttpResponse('<h1>This is from class based view</h1>')
    
class HelloWorldTemplateView(TemplateView):

    template_name = 'myApp/result.html'

class HelloWorldTemplateContextView(TemplateView):

    template_name = 'myApp/info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Anand'
        context['sub'] = 'Python'
        context['marks'] = 100

        return context
