# Generated by Django 3.0.3 on 2020-02-25 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20200224_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='comment_count',
            field=models.IntegerField(default=0, verbose_name='评论数'),
        ),
        migrations.AddField(
            model_name='movie',
            name='like_count',
            field=models.IntegerField(default=0, verbose_name='点赞数'),
        ),
    ]
