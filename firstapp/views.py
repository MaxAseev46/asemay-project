from django.shortcuts import render
from .forms import UserForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

# Create your views here.


# def index(request):
#     header = "Персональные данные"  # обычная переменная     
#     langs = ["Английский", "Немецкий", "Испанский"]  # массив     
#     user = {"name": "Максим,", "age": 30}  # словарь     
#     addr = ("Виноградная", 23, 45)  # кортеж 
#     data = {"header": header, "langs": langs, "user": user, "address": addr}     
#     return render(request, "index.html", context=data) 

# def index(request):
#  return render(request, "firstapp/index.html")
 
# def index(request):
#     data = {"age": 66}
#     return render(request, "firstapp/index.html", context=data)

#def index(request):
# cat = ["Ноутбуки", "Принтеры", "Сканеры", "Диски", "Шнуры"]
# return render(request, "firstapp/index.html", context={"cat": cat})

def index(request: HttpRequest):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        output = "<h2>Пользователь</h2><h3>Имя - {0}, Возраст - {1}</h3>".format(name, age)
        return HttpResponse(output)
    else:
        userform = UserForm()
        return render(request, "firstapp/index.html", {"form": userform})

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
