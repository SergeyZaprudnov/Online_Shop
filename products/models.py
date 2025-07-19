from django.db import models


class Category(models.Model):
    """ Модель категорий"""
    name = models.CharField(max_length=100, verbose_name='Наименование')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    """Модель товара"""
    name = models.CharField(max_length=150, verbose_name='Наименование')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    image = models.ImageField(upload_to='media/products/', null=True, blank=True, verbose_name='Изображение')

    def __str__(self):
        return f'{self.name}{self.category}{self.description}{self.price}{self.image}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

