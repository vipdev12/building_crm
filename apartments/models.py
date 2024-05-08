from django.db import models

# Create your models here.


class Apartment(models.Model):
    STATUS_CHOICES = (
        ('активно', 'Активно'),
        ('бронь', 'Бронь'),
        ('куплено', 'Куплено'),
        ('рассрочка', 'Рассрочка'),
        ('бартер', 'Бартер'),
    )

    floor = models.PositiveIntegerField()
    object_name = models.CharField(max_length=100, null=True, blank=True)
    square_meters = models.FloatField(null=True, blank=True)
    date = models.DateField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='активно')
    client_name = models.CharField(max_length=40, default='-')
    client_number = models.CharField(max_length=30, default='-')

    def __str__(self):
        return f"{self.object_name} - Floor {self.floor}"
