# Generated by Django 3.0.3 on 2020-02-19 15:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mail_receiver', to=settings.AUTH_USER_MODEL, verbose_name='收件人'),
        ),
        migrations.AlterField(
            model_name='mail',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mail_sender', to=settings.AUTH_USER_MODEL, verbose_name='发送人'),
        ),
    ]
