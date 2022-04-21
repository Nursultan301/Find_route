from django.db import models
from django.urls import reverse


class City(models.Model):
    """ Город """
    name = models.CharField('Город', max_length=100, unique=True)

    objects = models.Manager

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
