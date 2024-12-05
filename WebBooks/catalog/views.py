from django.shortcuts import render 
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Book, Author, BookInstance, Genre
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .forms import AuthorsForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .forms import Form_add_author
from django.urls import reverse
from .forms import Form_edit_author

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

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {'text_head': text_head,
        'books': books, 'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'authors': authors, 'num_authors': num_authors,
        'num_visits': num_visits
        }

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
 if request.method == 'POST':
    form = Form_add_author(request.POST, request.FILES)
    if form.is_valid():
        # получить данные из формы
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        date_of_birth = form.cleaned_data.get("date_of_birth")
    about = form.cleaned_data.get("about")
    photo = form.cleaned_data.get("photo")
    # создать объект для записи в БД
    obj = Author.objects.create(
    first_name=first_name,
    last_name=last_name,
    date_of_birth=date_of_birth,
    about=about,
    photo=photo)
    # сохранить полученные данные
    obj.save()
    # загрузить страницу со списком автором
    return HttpResponseRedirect(reverse('authors-list'))
 else:
    form = Form_add_author()
    context = {"form": form}
    return render(request, "catalog/authors_add.html", context)


    # author = Author.objects.all()
    # authorsform = AuthorsForm()
    # return render(request, "catalog/authors_add.html",
    #         {"form": authorsform, "author": author})

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
 success_url = reverse_lazy('edit_books')

class BookUpdate(UpdateView):
    model = Book
    fields =  '__all__'
    success_url= reverse_lazy('edit_books')

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('edit_books')

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

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
 # Универсальный класс представления списка книг,
 # находящихся в заказе у текущего пользователя
 model = BookInstance
 template_name = 'catalog/bookinstance_list_borrowed_user.html'
 paginate_by = 10
 
 def get_queryset(self):
    return BookInstance.objects.filter(
        borrower=self.request.user).filter(
        status__exact='2').order_by('due_back')

def edit_authors(request):
 author = Author.objects.all()
 context = {'author': author}
 return render(request, "catalog/edit_authors.html", context)


def edit_author(request, id):
 author = Author.objects.get(id=id)
 # author = get_object_or_404(Author, pk=id)
 if request.method == "POST":
    instance = Author.objects.get(pk=id)
    form = Form_edit_author(request.POST, request.FILES, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/edit_authors/")
    else:
        form = Form_edit_author(instance=author)
        content = {"form": form}
        return render(request, "catalog/edit_author.html", content)

def edit_books(request):
 book = Book.objects.all()
 context = {'book': book}
 return render(request, "catalog/edit_books.html", context)