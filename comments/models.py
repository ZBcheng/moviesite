from django.db import models

from movies.models import Movie
from users.models import UserProfile
# Create your models here.


class Comment(models.Model):
    '''评论'''

    content = models.TextField(verbose_name='评论内容')
    publisher = models.ForeignKey(
        UserProfile, verbose_name='发布人', on_delete=models.CASCADE)
    link_movie = models.ForeignKey(
        Movie, verbose_name='关联电影', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.publisher.username) + ": [" + str(self.link_movie.name) + ']' + str(self.content)[:10]
