from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class Homepage(TemplateView):
    template_name = "pages/index.html"


class AboutUs(TemplateView):
    template_name = "pages/about.html"

class Service(TemplateView):
    template_name = "pages/service.html"

class Contact(TemplateView):
    template_name = "pages/contact.html"



