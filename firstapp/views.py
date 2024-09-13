from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

# Create your views here.


# def index(request):
#     header = "Персональные данные"  # обычная переменная     
#     langs = ["Английский", "Немецкий", "Испанский"]  # массив     
#     user = {"name": "Максим,", "age": 30}  # словарь     
#     addr = ("Виноградная", 23, 45)  # кортеж 
#     data = {"header": header, "langs": langs, "user": user, "address": addr}     
#     return render(request, "index.html", context=data) 

def index(request):
 return render(request, "firstapp/index.html")
 

#def about(request):
#    return HttpResponse("<h2>About</h2>")

#def contact(request):
#    return HttpResponseRedirect("/about")

def details(request):
    return HttpResponsePermanentRedirect("/")

def products(request, productid=1): 
    output = "<h2>Продукт № {0}</h2>".format(productid) 
    return HttpResponse(output) 
 
def users(request, id=1, name='Максим'):     
    output = "<h2>Пользователь</h2><h3>id: {0}                   Имя: {1}</h3>".format(id, name) 
    return HttpResponse(output) 
