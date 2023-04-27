from django.db import models

class Film(models.Model):
    GENRE = (
        ('Ужасы', "Ужасы"),
        ('Мелодраммы', 'Мелодраммы'),
        ('Комедии', 'Комедии'),
        ('Фантастика', "Фантастика")

    )
    title = models.CharField("Название фильма", max_length=100)
    image = models.ImageField("Фото", upload_to='')
    description = models.TextField('Описание фильма')
    genre = models.CharField('Жанр фильма', max_length=100, choices=GENRE)
    quantity = models.PositiveIntegerField('Колличество серий')
    trailer = models.URLField('Трейлер')
    name = models.CharField(max_length=100, blank=True)
    year = models.DateField(auto_now_add=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Reviews(models.Model):
    RATING = (
        ('*', '*'),
        ('**', '**'),
        ('***', '***'),
        ('****', '****'),
        ('*****', '*****')
    )
    film_choice_comment = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='comment_object')
    name = models.CharField(max_length=50)
    stars = models.CharField(max_length=100, choices=RATING)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Оценка фильма'
        verbose_name_plural = 'Оценки фильмов'

