# Generated by Django 3.0.3 on 2020-02-23 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20200214_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='stars',
            field=models.IntegerField(default=0, verbose_name='评级'),
        ),
    ]
