from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from . models import Project,ProjectCategory
# Create your views here.


class Homepage(TemplateView):
    template_name = "pages/index.html"


class AboutUs(TemplateView):
    template_name = "pages/about.html"

class Service(TemplateView):
    template_name = "pages/service.html"

class Contact(TemplateView):
    template_name = "pages/contact.html"


class WorkListView(ListView):
    model = Project
    template_name = "pages/work.html"
    context_object_name =  "work"
    
    def get_context_data(self, **kwargs):
        context = super(WorkListView, self).get_context_data(**kwargs)
        context["category"] = ProjectCategory.objects.all()
        return context
    

class WorkDetailView(DetailView):
    model = Project
    context_object_name =  "work"
    template_name = "pages/work-detail.html"

    
    def get_context_data(self, **kwargs):
        context = super(WorkDetailView, self).get_context_data(**kwargs)
        # context["next"] = Project.objects.get('?')
        return context
    
