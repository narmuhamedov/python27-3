# Generated by Django 4.2 on 2023-04-13 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название фильма')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
                ('description', models.TextField(verbose_name='Описание фильма')),
                ('genre', models.CharField(choices=[('Ужасы', 'Ужасы'), ('Мелодраммы', 'Мелодраммы'), ('Комедии', 'Комедии'), ('Фантастика', 'Фантастика')], max_length=100, verbose_name='Жанр фильма')),
                ('quantity', models.PositiveIntegerField(verbose_name='Колличество серий')),
                ('trailer', models.URLField(verbose_name='Трейлер')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]