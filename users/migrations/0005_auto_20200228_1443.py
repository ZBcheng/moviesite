# Generated by Django 3.0.3 on 2020-02-28 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_userprofile_saved_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, default='avatar/sausages.jpg', upload_to='avatar', verbose_name='头像'),
        ),
    ]
