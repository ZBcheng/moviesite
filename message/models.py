from django.db import models

from users.models import UserProfile

# Create your models here.


MESSAGE_STATUS = (
    ('0', '未读'),
    ('1', '已读'),
    ('2', '信息')
)


class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    message_title = models.CharField(max_length=100,
                                     verbose_name='信息标题', blank=True, null=True)
    message_content = models.TextField(verbose_name='信息内容')
    message_status = models.CharField(
        verbose_name='信息状态', max_length=15, choices=MESSAGE_STATUS, default='0')
    sender = models.ForeignKey(
        UserProfile, related_name="sender", on_delete=models.CASCADE, verbose_name='发件人')
    receiver = models.ManyToManyField(
        UserProfile, related_name="receiver", verbose_name='收件人')

    send_time = models.DateField(verbose_name='发送日期', auto_now=True)

    class Meta:
        verbose_name = '信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message_title
