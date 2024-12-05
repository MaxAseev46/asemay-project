from django.contrib import admin
from django.utils.html import format_html
from.models import Author, Book, Genre, Language,\
    Publisher, Status, BookInstance

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
  list_display = ('last_name', 'first_name', 'photo', )
  fields = ['first_name', 'last_name',
    ('date_of_birth', 'date_of_death', 'photo')]
  readonly_fields = ["show_photo"]
  def show_photo(self,obj):
     return format_html(
        f'<img src="{obj.photo.url}" style="max-height: 100px;">')
  show_photo.short_description = 'Фото'
  
admin.site.register(Author,AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book) 
class BookAdmin(admin.ModelAdmin):
  list_display = ('title', 'genre', 'language', 'display_author', 'show_photo')
  list_filter = ('genre', 'author')
  inlines = [BooksInstanceInline]
  readonly_fields = ["show_photo"]
  def show_photo(self, obj):
    return format_html(
       f'<img src="{obj.photo.url}" style="max-height: 100px;">')
  show_photo.short_description = 'Обложка'


@admin.register(BookInstance)
class BookinstanceAdmin(admin.ModelAdmin): 
   list_filter = ('book', 'status')
   fieldsets = (
    ('Экземпляр книги', {
     'fields': ('book', 'imprint', 'inv_nom')
    }),
    ('Статус и окончание его действия', {
    'fields': ('status', 'due_back')
    }),
)


# admin.site.register(Author, AuthorAdmin)
# admin.site.register(Book)
admin.site.register(Genre) 
admin.site.register(Language) 
admin.site.register(Publisher)
admin.site.register(Status) 
# admin.site.register(BookInstance)