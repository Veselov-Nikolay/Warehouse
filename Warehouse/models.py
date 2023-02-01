from django.db import models

# Create your models here.
from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название склада')
    volume = models.FloatField(verbose_name='Объем')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Склады'
        verbose_name = 'Склад'
        ordering = ['name']

class Shelf(models.Model):
    number = models.PositiveIntegerField(verbose_name='Номер стеллажа')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Склад')
    storage_capacity = models.PositiveIntegerField(verbose_name='Вместимость')
    height = models.FloatField(verbose_name='Высота')
    width = models.FloatField(verbose_name='Ширина')
    length = models.FloatField(verbose_name='Длина')
    max_load = models.FloatField(verbose_name='Максимальная нагрузка')

    class Meta:
        verbose_name_plural = 'Стеллажи'
        verbose_name = 'Стеллаж'
        ordering = ['number']

class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название организации')
    bank_details = models.TextField(verbose_name='Банковские реквизиты')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиент'
        ordering = ['name']

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название товара')
    height = models.FloatField(verbose_name='Высота')
    width = models.FloatField(verbose_name='Ширина')
    length = models.FloatField(verbose_name='Длина')
    weight = models.FloatField(verbose_name='Вес')
    arrival_date = models.DateField(verbose_name='Дата поступления')
    contract_number = models.PositiveIntegerField(verbose_name='Номер договора')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    contract_end_date = models.DateField(verbose_name='Дата окончания договора')
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE, verbose_name='Стеллаж')
    position = models.PositiveIntegerField(verbose_name='Позиция')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        ordering = ['height']

# class Item(models.Model):
#     height = models.PositiveIntegerField()
#     width = models.PositiveIntegerField()
#     length = models.PositiveIntegerField()
#     weight = models.PositiveIntegerField()
#     arrival_date = models.DateField()
#     contract_number = models.PositiveIntegerField()
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)
#     end_date = models.DateField()
#     shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
#     position = models.PositiveIntegerField()

