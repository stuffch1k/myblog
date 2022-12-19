from django.db import models
from django.urls import reverse

from django.contrib.auth.models import AbstractUser

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=255, verbose_name='Заголовок')
    content=models.TextField(blank=True, null=True, verbose_name='Описание')
    photo=models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фотография')
    time_create=models.DateTimeField(auto_now_add=True)
    time_update=models.DateTimeField(auto_now=True)
    is_published=models.BooleanField(default=True, verbose_name='Активен')
    category=models.ForeignKey('Category',on_delete=models.CASCADE,null=True, verbose_name='Категория')
    likes=models.ManyToManyField('CustomUser',blank=True,null=True, verbose_name="Лайки")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Пост'
        verbose_name_plural='Посты'

    def get_absolute_url(self):
        return reverse('detail_post', kwargs={'pk':self.pk})

class Category(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'
    
class CustomUser(AbstractUser):
    biography=models.TextField(verbose_name='Биография', blank=True, null=True)
    avatar=models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Аватарка', blank=True, null=True)
    # userslug=models.SlugField(blank=True,null=True)

    def __str__(self):
        return self.username
    def get_absolute_url(self):
        return reverse("my_profile", kwargs={"username": self.username})

class Comment(models.Model):
    author=models.ForeignKey('CustomUser', on_delete=models.CASCADE, verbose_name='Автор',)
    post=models.ForeignKey('Blog',on_delete=models.CASCADE, verbose_name='Пост',)
    text=models.TextField(verbose_name='Текст')

    def __str__(self):
        return f"Комментарий {self.author} для поста {self.post}"

    class Meta:
        verbose_name='Комментарий'
        verbose_name_plural='Комментарии'
    