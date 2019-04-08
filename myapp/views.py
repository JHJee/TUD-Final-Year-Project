from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Example, Person
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from .forms import Form1, Form2
import json

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

class Form1View(FormView):
    form_class = Form1
    template_name = 'demo.html'
    success_url = '/form-success/' 
    
    def form_invalid(self, form):
        response = super(Form1View, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(Form1View, self).form_valid(form)
        example_list = list(Example.objects.all())
        stno_list = []
        if self.request.is_ajax():
            print(form.cleaned_data)
            inputData = form.cleaned_data['st_no']
            print(inputData)
            for example in example_list:
                stno_list.append(example.st_no)
            print(stno_list)
            reply = inputData in stno_list
            print(reply)

            data = {
                    'message': "Successfully submitted form data.",
                    'data': form.cleaned_data,
                    'reply': reply,
                    }
            return JsonResponse(data)
        else:
            return response

class Form2View(FormView):
    form_class = Form2
    template_name = 'demo2.html'
    success_url = '/form-success/'

    def form_invalid(self, form):
        response = super(Form2View, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response
    def form_valid(self, form):
        response = super(Form2View, self).form_valid(form)
        #example_list = list(Example.objects.all()) 
        #print(json.dumps(list(Example.objects.values())))
        example_list = {}

        if self.request.is_ajax():
            print(form.cleaned_data)
            inputData = form.cleaned_data['st_no']
            
            reply = None
            query = "SELECT * FROM example WHERE st_no LIKE '"+inputData+"\'"
            print(query)
            result = Example.objects.raw(query)
            print(result)
            for r in result:
                print(r)
            reply = bool(len(list(result)))
            
            for x in Example.objects.values():
                example_list[str(x['id'])] = { 'st_no':x['st_no'], 'name':x['name'], 'age':x['age'] }

            print(example_list)

            data = {
                    'message': "Successfully submitted form data.",
                    'data': form.cleaned_data,
                    'example_list': json.dumps(example_list),
                    'reply': reply,
                    }
            return JsonResponse(data)
        else:
            return response


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

class Overview(TemplateView):
    template_name = 'overview.html'
class LessonPlan(TemplateView):
    template_name = 'lesson-plan.html'
class LessonA(TemplateView):
    template_name = 'lesson-a.html'
class LessonB(TemplateView):
    template_name = 'lesson-b.html'
class LessonC(TemplateView):
    template_name = 'lesson-c.html'

