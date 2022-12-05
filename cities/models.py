from django.db import models
from django.urls import reverse


class City(models.Model):
    title = models.CharField("Называние", max_length=50, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('cities:detail', kwargs={'pk': self.pk})
