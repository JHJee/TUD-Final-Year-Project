from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Example, Person
from django.http import HttpResponse
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render( request, 'index.html')

class AboutPageView(TemplateView):
    template_name = "about.html"
    def about(request):
        num_row = Person.objects.using('mongo').all().count()
        example_list = list(Example.objects.all())
        person_list = list(Person.objects.using('mongo').all())
        return render( request, 'about.html', context={'num_row': num_row, 'example_list': example_list, 'person_list': person_list}, )

class ExampleView(DetailView):
    model = Example

class ExampleCreate(CreateView):
    model = Example
    fields = ['id', 'st_no', 'name', 'age']
    success_url = reverse_lazy('index')

class ExampleUpdate(UpdateView):
    model = Example
    fields = ['id', 'st_no', 'name', 'age']
    success_url = reverse_lazy('index')

class ExampleDelete(DeleteView):
    model = Example
    success_url = reverse_lazy('index')

class Main(TemplateView):
    template_name = "main.html"
class RDBMS(TemplateView):
    template_name = "rdbms-main.html"
class SQLInjection(TemplateView):
    template_name = "sql-injection.html"
class PrivilegeAbuse(TemplateView):
    template_name = "privilege-abuse.html"
class Unencrypted(TemplateView):
    template_name = "unencrypted.html"
