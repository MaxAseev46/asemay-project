from django.shortcuts import render 
from django.http import HttpResponse 
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from .forms import AuthorsForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Book
 
# Create your views here. 
def index(request):
    text_head = 'На нашем сайте вы можете получить книги в электронном виде'
    books = Book.objects.all()
    num_books = Book.objects.all().count()

    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(
        status__exact=2).count()
    
    authors = Author.objects
    num_authors = Author.objects.count()

    context = {'text_head': text_head,
        'books': books, 'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'authors': authors, 'num_authors': num_authors}

    return render(request, 'catalog/index.html', context)
    # return HttpResponse("Главная страница сайта Мир книг!")
    # # Генерация "количеств" некоторых главных объектов
    # num_books = Book.objects.all().count()
    # num_instances = BookInstance.objects.all().count()
    # # Доступные книги (статус = 'На складе')
    # # Здесь метод 'all()' применен по умолчанию.
    # num_instances_available = BookInstance.objects.filter(status__exact=2).count()
    # # Авторы книг,
    # num_authors = Author.objects.count()
    # # Отрисовка HTML-шаблона index.html с данными
    # # внутри переменной context
    # return render(request, 'index.html', context={
    # 'num_books': num_books,
    # 'num_instances': num_instances,
    # 'num_instances_available': num_instances_available,
    # 'num_authors': num_authors}) 

def authors_add(request):
    author = Author.objects.all()
    authorsform = AuthorsForm()
    return render(request, "catalog/authors_add.html",
            {"form": authorsform, "author": author})

def create(request):
    if request.method == "POST":
        author = Author()
        author.first_name = request.POST.get("first_name")
        author.last_name = request.POST.get("last_name")
        author.date_of_birth = request.POST.get("date_of_birth")
        author.date_of_death = request.POST.get("date_of_death")
        author.save()
        return HttpResponseRedirect("/authors_add/")
    
def edit1(request, id):
    author = Author.objects.get(id=id)
    if request.method == "POST":
        author.first_name = request.POST.get("first_name")
        author.last_name = request.POST.get("last_name")
        author.date_of_birth = request.POST.get("date_of_birth")
        author.date_of_death = request.POST.get("date_of_death")
        author.save()
        return HttpResponseRedirect("/authors_add/")
    else:
        return render(request, "edit1.html", {"author": author})

def delete(request, id):
    try:
        author = Author.objects.get(id=id)
        author.delete()
        return HttpResponseRedirect("/authors_add/")
    except Author.DoesNotExist:
        return HttpResponseNotFound("<h2>Автор не найден</h2>")

class BookDetailView(generic.DetailView):
    model = Book

class BookListView(generic.ListView):
    model = Book
    paginate_by = 3

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4

class BookCreate(CreateView):
 model = Book
 fields = '__all__'
 success_url = reverse_lazy('books')

 class BookUpdate(UpdateView):
     model = Book
     fields =  '__all__'
     success_url= reverse_lazy('books')

     class BookDelete(DeleteView):
         model = Book
         success_url = reverse_lazy('books')

class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    paginate_by = 3

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'

class AuthorListView(ListView):
    model = Author
    paginate_by = 4

class AuthorDetailView(DetailView):
    model = Author

def about(request):
    text_head = 'Сведения о компании'
    name = 'ООО "Интеллектуальные информационные системы"'
    rab1 = 'Разработка приложений на основе' \
    ' систем искусственного интеллекта'
    rab2 = 'Распознавание объектов дорожной инфраструктуры'
    rab3 = 'Создание графических АРТ-объектов на основе' \
    ' систем искусственного интеллекта'
    rab4 = 'Создание цифровых интерактивных книг, учебных пособий' \
    ' автоматизированных обучающих систем'
    context = {'text_head': text_head, 'name': name,
    'rab1': rab1, 'rab2': rab2,
    'rab3': rab3, 'rab4': rab4}
    # передача словаря context с данными в шаблон
    return render(request, 'catalog/about.html', context)
def contact(request):
 text_head = 'Контакты'
 name = 'ООО "Интеллектуальные информационные системы"'
 address = 'Москва, ул. Планерная, д.20, к.1'
 tel = '495-345-45-45'
 email = 'iis_info@mail.ru'
 # Словарь для передачи данных в шаблон index.html
 context = {'text_head': text_head,
 'name': name, 'address': address,
 'tel': tel,
 'email': email}
 # передача словаря context с данными в шаблон
 return render(request, 'catalog/contact.html', context)