# Generated by Django 4.2 on 2024-12-05 21:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите наименование издательства', max_length=20, verbose_name='Издательство')),
            ],
        ),
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back']},
        ),
        migrations.RemoveField(
            model_name='author',
            name='date_of_death',
        ),
        migrations.AddField(
            model_name='author',
            name='about',
            field=models.TextField(help_text='Введите сведения об авторе', null=True, verbose_name='Сведения об авторе'),
        ),
        migrations.AddField(
            model_name='author',
            name='photo',
            field=models.ImageField(blank=True, help_text='Введите фото автора', null=True, upload_to='images', verbose_name='Фото автора'),
        ),
        migrations.AddField(
            model_name='book',
            name='photo',
            field=models.ImageField(help_text='Введите изображение обложки', null=True, upload_to='images', verbose_name='Изображение обложки'),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='Введите цену книги', max_digits=7, null=True, verbose_name='Цена (руб.)'),
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='borrower',
            field=models.ForeignKey(blank=True, help_text='Выберите заказчика книги', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Заказчик'),
        ),
    ]
