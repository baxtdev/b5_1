from django.db import models

# Create your models here.

class Stock(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Название',
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
    )
    langitude = models.FloatField(
        verbose_name='',
    )
    latitude = models.FloatField(
        verbose_name='',
    )


    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склад'
     
