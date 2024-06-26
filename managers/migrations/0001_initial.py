# Generated by Django 5.0.4 on 2024-05-06 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('phone_number', models.CharField(max_length=100, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('quantity_sell', models.IntegerField(blank=True, default=0, null=True, verbose_name='Кол-во сделок')),
                ('password', models.CharField(blank=True, max_length=100, null=True, verbose_name='Временный пароль')),
            ],
        ),
    ]
