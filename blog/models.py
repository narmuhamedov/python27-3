from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'