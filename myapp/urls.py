# myapp/urls.py
from django.urls import path, re_path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.AboutPageView.about, name='about'),
    path('create', views.ExampleCreate.as_view(), name='example_create'),
    path('view/ <int:pk>', views.ExampleView.as_view(), name='example_view'),
    path('edit/<int:pk>', views.ExampleUpdate.as_view(), name='example_edit'),
    path('delete/<int:pk>', views.ExampleDelete.as_view(), name='example_delete'),
    path('overview/', views.Overview.as_view(), name='overview'),
    path('overview/lesson-plan/', views.LessonPlan.as_view(), name='lesson-plan'),
    path('overview/lesson-plan/lesson-A', views.LessonA.as_view(), name='lesson-a'),
    path('overview/lesson-plan/lesson-B', views.LessonB.as_view(), name='lesson-b'),
    path('overview/lesson-plan/lesson-C', views.LessonC.as_view(), name='lesson-c'),
    path('demo/', views.Form1View.as_view(), name='demo'),
    path('demo2/', views.Form2View.as_view(), name='demo2'),
]
