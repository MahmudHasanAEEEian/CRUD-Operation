from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import Person
from .forms import PersonCreateForm
from django.template.loader import render_to_string
# Create your views here.

def Index(request):
    
    person_list = Person.objects.all()
    
    if request.method == 'POST':
        
        form = PersonCreateForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect(request.path_info)
        
        else:
            form = PersonCreateForm()
            return redirect(request.path_info)

    else:
        
        context = {
            'person_list': person_list
        }

        return render(request, 'index.html', context)

def person_create(request):

    data = dict()

    if request.method=='POST':
        
        form = PersonCreateForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            
            person_list = Person.objects.all()
            context = {
                'person_list': person_list
            }

            data['valid'] = True
            data['success'] = render_to_string('success/create-success.html')
            data['person_list'] = render_to_string('person/person_list.html', context)
            return JsonResponse(data)
        
        else:

            data['html_form'] = render_to_string('person/person_create.html')
            return JsonResponse(data)

    else:

        data['html_form'] = render_to_string('person/person_create.html')
        return JsonResponse(data)

def person_edit(request, id):

    data = dict()

    person = Person.objects.get(id=id)
    
    person_dic = {
            'person': person
        }

    if request.method=='POST':
        
        form = PersonCreateForm(request.POST, request.FILES, instance=person)
        
        if form.is_valid():
            form.save()
            
            person_list = Person.objects.all()
            context = {
                'person_list': person_list
            }

            data['valid'] = True
            data['success'] = render_to_string('success/edit-success.html')
            data['person_list'] = render_to_string('person/person_list.html', context)
            return JsonResponse(data)
        
        else:
   
            data['edit_form'] = render_to_string('person/person_edit.html', person_dic)
            return JsonResponse(data)

    else:

        data['edit_form'] = render_to_string('person/person_edit.html', person_dic)
        return JsonResponse(data)


def person_delete(request, id):

    data = dict()

    person = Person.objects.get(id=id)
    
    person_dic = {
            'person': person
        }

    if request.method=='POST':
        
        person.delete()
        
        person_list = Person.objects.all()
        context = {
            'person_list': person_list
        }
        data['valid'] = True
        data['success'] = render_to_string('success/delete-success.html')
        data['person_list'] = render_to_string('person/person_list.html', context)
        return JsonResponse(data)
        
    else:

        data['delete_form'] = render_to_string('person/person_delete.html', person_dic)
        return JsonResponse(data)