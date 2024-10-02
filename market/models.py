from django.db import models

from django.db import models
from django.contrib.auth.models import User


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    store_name = models.CharField(max_length=255, verbose_name='Название магазина')
    rating = models.FloatField(default=0.0, verbose_name='Рейтинг')

    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'

    def __str__(self):
        return self.store_name

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Родительская категория')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, verbose_name='Продавец')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=255, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE, verbose_name='Товар')
    image = models.ImageField(upload_to='product_images/', verbose_name='Изображение')
    is_main = models.BooleanField(default=False, verbose_name='Главное изображение')

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товаров'

    def __str__(self):
        return f"Image for {self.product.name}"


class Attribute(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название атрибута')

    class Meta:
        verbose_name = 'Атрибут'
        verbose_name_plural = 'Атрибуты'

    def __str__(self):
        return self.name


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, related_name='product_attributes', on_delete=models.CASCADE, verbose_name='Товар')
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, verbose_name='Атрибут')
    value = models.CharField(max_length=255, verbose_name='Значение')

    class Meta:
        verbose_name = 'Атрибут товара'
        verbose_name_plural = 'Атрибуты товаров'

    def __str__(self):
        return f"{self.attribute.name}: {self.value}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Общая сумма')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    class Meta:
        verbose_name = 'Заказанный товар'
        verbose_name_plural = 'Заказанные товары'

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE, verbose_name='Товар')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    rating = models.PositiveIntegerField(verbose_name='Рейтинг')
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f"Review for {self.product.name} by {self.user.username}"


