from django.db import models
from django.urls import reverse

class auth(models.Model):
    nickname = models.CharField(max_length=255, verbose_name='Нікнейм')
    email = models.CharField(max_length=255, verbose_name='Електронний адрес')
    password = models.CharField(max_length=255, verbose_name='Пароль')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата реєстрації')

    def __str__(self) -> str:
        return self.nickname
    
    def get_absolute_url(self):
        return reverse('user', kwargs={'user_id': self.pk})
    
    class Meta:
        verbose_name = 'Профіль'
        verbose_name_plural = 'Профілі'
        ordering = []