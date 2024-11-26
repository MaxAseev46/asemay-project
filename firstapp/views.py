from django.shortcuts import render
from .forms import UserForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound

# Create your views here.

def index(request):
    my_kv = ['I квартал ->', 'II квартал ->', 'III квартал->',
    'IV квартал->']
    my_month = ['Январь', 'Февраль', 'Март',
    'Апрель', 'Май', 'Июнь',
    'Июль', 'Август', 'Сентябрь',
    'Октябрь', 'Ноябрь', 'Декабрь']
    context = {'my_month': my_month, 'my_kv': my_kv}
    return render(request, "firstapp/index.html", context)

def about(request):
    return render(request, "firstapp/about.html")

def contact(request):
    return render(request, "firstapp/contact.html")

def details(request):
    return HttpResponsePermanentRedirect("/")

def products(request, productid=1): 
    output = "<h2>Продукт № {0}</h2>".format(productid) 
    return HttpResponse(output) 
 
def users(request, id=1, name='Максим'):     
    output = "<h2>Пользователь</h2><h3>id: {0}                   Имя: {1}</h3>".format(id, name) 
    return HttpResponse(output) 
