from django.db import models


class City(models.Model):
    title = models.CharField("Называние", max_length=50, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['title']
