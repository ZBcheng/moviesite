from django.db import models
from django.contrib.auth.models import AbstractUser

from movies.models import Movie

# Create your models here.


class UserProfile(AbstractUser):
    '''用户信息表'''
    phone = models.CharField(
        max_length=30, verbose_name='手机', blank=True, null=True)
    username = models.CharField(
        max_length=20, verbose_name='用户名', unique=True, blank=True)
    avatar = models.ImageField(
        verbose_name='头像', blank=True, default='/upload/avatar/sausages.jpg')
    email = models.EmailField(max_length=30, verbose_name='邮箱', unique=True)
    password = models.CharField(max_length=150, verbose_name='密码')
    stored_movies = models.ManyToManyField(
        Movie, verbose_name='收藏电影', blank=True, null=True)

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
