from django.db import models

# Create your models here.


class Apartment(models.Model):
    number = models.IntegerField(verbose_name='№ квартиры')
    category = models.CharField(max_length=20, verbose_name='Объект')
    floor = models.IntegerField(verbose_name='Этаж')
    square = models.CharField(max_length=100, verbose_name='КВ')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    status = models.CharField(max_length=100, verbose_name='Статус')
    price = models.CharField(max_length=100, verbose_name='Цена')
    client = models.CharField(max_length=100, null=True, blank=True, default='-', verbose_name='Клиент')
    status = models.CharField(max_length=100, default='-', null=True, blank=True, verbose_name='Статус')
    client_number = models.CharField(max_length=100, null=True, blank=True, default='-', verbose_name='Номер клиента')
    contract_number = models.IntegerField(verbose_name='№ Договора', null=True, blank=True)

    def __str__(self):
        return f'№ {str(self.number)}'


