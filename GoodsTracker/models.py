from django.db import models

class Category(models.Model):
    """Категории товара"""
    name = models.CharField("Категория", max_length=30)
    url = models.SlugField(max_length=160)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Store(models.Model):
    """Магазины"""
    name = models.CharField("Название", max_length=30)
    inn = models.CharField("ИНН", max_length=10)
    url = models.SlugField(max_length=160)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class Product(models.Model):
    """Товар"""
    name = models.CharField('Товар', max_length=50)
    price = models.DecimalField('Стоимость', max_digits=8,
        decimal_places=2)
    amount = models.PositiveSmallIntegerField('Количество товара')
    price_for_one = models.DecimalField('Цена за штуку', max_digits=8,
        decimal_places=2)
    store = models.ForeignKey(Store, verbose_name='Магазин',
        on_delete=models.SET_NULL, null=True)
    purchaise_date = models.DateField('День покупки')
    category = models.ForeignKey(Category, verbose_name='Категория товара',
        on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'