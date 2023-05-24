# coding=utf-8

from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    id = models.AutoField(u'ID', primary_key=True)
    name = models.CharField(u'Название', max_length=64, null=False)
    price = models.DecimalField(u'Цена', max_digits=10, decimal_places=2)
    image = models.ImageField(u'Изображение', upload_to='phone_images/')
    release_date = models.DateField(u'Дата изготовления')
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(unique=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name