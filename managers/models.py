from django.db import models


# Create your models here.
class Manager(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО')
    phone_number = models.CharField(max_length=100, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Почта')
    date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    quantity_sell = models.IntegerField(verbose_name='Кол-во сделок', null=True, blank=True, default=0)
    password = models.CharField(max_length=100, null=True, blank=True, verbose_name='Временный пароль')

    def __str__(self):
        return f'Name: {self.name}; phone_number: {self.phone_number}'