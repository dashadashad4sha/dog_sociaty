from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(blank=False, verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото', null=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано?')
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.PROTECT, blank=False)
    view = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название категории', db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['title']


class Doggy(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    poroda = models.CharField(max_length=150, verbose_name='Порода', default='')
    content = models.TextField(blank=True, verbose_name='Биография')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото', null=True)
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.PROTECT, blank=True, default=1)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Клички"
        verbose_name_plural = "Клички"
        ordering = ['id']
