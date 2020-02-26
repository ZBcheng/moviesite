from django.db import models

from users.models import UserProfile
# Create your models here.


class Mail(models.Model):
    title = models.CharField(verbose_name='标题', max_length=20)
    content = models.TextField(verbose_name='内容')
    sender = models.ForeignKey(
        UserProfile, related_name='mail_sender', verbose_name='发送人', on_delete=models.CASCADE)
    receiver = models.ForeignKey(
        UserProfile, related_name='mail_receiver', verbose_name='收件人', on_delete=models.CASCADE)
    send_time = models.DateField(auto_now=True, verbose_name='发送日期')

    class Meta:
        verbose_name = '信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '[' + str(self.sender.username) + ']' + self.title
