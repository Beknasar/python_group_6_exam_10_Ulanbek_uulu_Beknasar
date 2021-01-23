from django.db import models
from accounts.models import Profile


class Messages(models.Model):
    from_user = models.ForeignKey(Profile, related_name='from_user', on_delete=models.CASCADE, verbose_name='от_пользователя')
    to_user = models.ForeignKey(Profile, related_name='to_user', on_delete=models.CASCADE, verbose_name='к_пользователю')
    pub_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=2000,  verbose_name='Текст сообщения')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'