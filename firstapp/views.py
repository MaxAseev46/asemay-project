from django.shortcuts import render
from .forms import UserForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound
from .models import Person

# Create your views here.

def index(request): 
    people = Person.objects.all()     
    return render(request, "firstapp/index.html", {"people": people})

def create(request):     
    if request.method == "POST": 
        klient = Person() 
        klient.name = request.POST.get("name")         
        klient.age = request.POST.get("age")         
        klient.save() 
    return HttpResponseRedirect("/")

# изменение данных в БД 
def edit(request, id):     
    try: 
        person = Person.objects.get(id=id)
        if request.method == "POST":             
            person.name = request.POST.get("name")             
            person.age = request.POST.get("age")             
            person.save()             
            return HttpResponseRedirect("/")         
        else: 
            return render(request, "firstapp/edit.html", {"person": person})     
    except Person.DoesNotExist: 
        return HttpResponseNotFound("<h2>Клиент не найден</h2>") 
 
# удаление данных из БД 
def delete(request, id):     
    try: 
        person = Person.objects.get(id=id)         
        person.delete()         
        return HttpResponseRedirect("/")     
    except Person.DoesNotExist: 
        return HttpResponseNotFound("<h2>Клиент не найден</h2>") 


def details(request):
    return HttpResponsePermanentRedirect("/")

def products(request, productid=1): 
    output = "<h2>Продукт № {0}</h2>".format(productid) 
    return HttpResponse(output) 
 
def users(request, id=1, name='Максим'):     
    output = "<h2>Пользователь</h2><h3>id: {0}                   Имя: {1}</h3>".format(id, name) 
    return HttpResponse(output) 
