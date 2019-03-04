# myapp/urls.py
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.AboutPageView.about, name='about'),
    path('create', views.ExampleCreate.as_view(), name='example_create'),
    path('view/ <int:pk>', views.ExampleView.as_view(), name='example_view'),
    path('edit/<int:pk>', views.ExampleUpdate.as_view(), name='example_edit'),
    path('delete/<int:pk>', views.ExampleDelete.as_view(), name='example_delete'),
    path('main/', views.Main.as_view(), name='main'),
    path('main/rdbms/', views.RDBMS.as_view(), name='rdbms'),
    path('main/rdbms/sql-injection', views.SQLInjection.as_view(), name='sql-injection'),
    path('main/rdbms/privilege-abuse', views.PrivilegeAbuse.as_view(), name='privilege-abuse'),
    path('main/rdbms/unencrypted-data', views.Unencrypted.as_view(), name='unencrypted'),
]
