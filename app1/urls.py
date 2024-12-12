from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    
    path('', views.Index, name='index'),
    path('person-create/', views.person_create, name='person_create'),
    path('person-edit/<id>/', views.person_edit, name='person_edit'),
    path('person-delete/<id>/', views.person_delete, name='person_delete'),

]
