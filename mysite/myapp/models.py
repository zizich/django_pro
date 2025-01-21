from django.db import models


class Product(models.Model):
  name = models.CharField(max_length=100, unique=True, verbose_name="Наименование")
  price = models.IntegerField(verbose_name="Цена")
  description = models.CharField(max_length=200, verbose_name="Описание")
  image = models.ImageField(blank=True, upload_to='images', verbose_name="Изображение")

  objects = models.Manager()

  def __str__(self):
      return self.name
  