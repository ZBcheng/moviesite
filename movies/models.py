from django.db import models

# Create your models here.


PERSON_CATEGORIES = (
    ('0', '演员'),
    ('1', '导演'),
    ('2', '导演/演员')
)


class Person(models.Model):
    '''导演/演员'''

    name = models.CharField(max_length=50, verbose_name='姓名')
    country = models.CharField(max_length=50, verbose_name='国籍')
    desc = models.TextField(verbose_name='简介')
    photo = models.ImageField(
        upload_to='person', verbose_name='照片', null=True, blank=True)
    category = models.CharField(
        choices=PERSON_CATEGORIES, max_length=10, verbose_name='人员类型', default='0')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '人员'
        verbose_name_plural = verbose_name


class MovieCategory(models.Model):
    '''电影类型'''
    name = models.CharField(max_length=10, verbose_name='类型', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '电影类型'
        verbose_name_plural = verbose_name


class Movie(models.Model):
    '''电影'''

    name = models.CharField(max_length=50, verbose_name='影片名')
    link_addr = models.CharField(max_length=100, verbose_name='链接地址')
    language = models.CharField(max_length=20, verbose_name='语言')
    area = models.CharField(max_length=10, verbose_name='地区')
    length = models.IntegerField(verbose_name='片长(分钟)')
    desc = models.TextField(verbose_name='简介')
    category = models.ManyToManyField(MovieCategory, verbose_name='类型')
    score = models.FloatField(verbose_name='评分', default=0)
    like_count = models.IntegerField(verbose_name='点赞数', default=0)
    comment_count = models.IntegerField(verbose_name='评论数', default=0)
    directors = models.ManyToManyField(
        Person, related_name='directors', verbose_name='导演')
    actors = models.ManyToManyField(
        Person, related_name='actors', verbose_name='演员')
    release_date = models.DateField(
        verbose_name='上映日期', null=True, blank=True)
    post = models.ImageField(
        upload_to='movie', verbose_name='电影封面', null=True)
    video = models.FileField(upload_to='video', verbose_name='视频', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '电影'
        verbose_name_plural = verbose_name
