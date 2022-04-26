from django.db import models
from django.core.exceptions import ValidationError


class Train(models.Model):
    name = models.CharField("Номер поезда", max_length=50, unique=True)
    travel_time = models.PositiveSmallIntegerField("Время в пути")
    from_city = models.ForeignKey("cities.City", on_delete=models.CASCADE,
                                  related_name='from_city_set',
                                  verbose_name='Из какого города')
    to_city = models.ForeignKey("cities.City", on_delete=models.CASCADE,
                                related_name='to_city_set',
                                verbose_name="В какой город")
    objects = models.Manager()

    class Meta:
        verbose_name = "Поезд"
        verbose_name_plural = "Поезда"
        ordering = ['travel_time']

    def __str__(self):
        return f'Поезд №{self.name} из города {self.from_city}'

    def clean(self):
        if self.from_city == self.to_city:
            raise ValidationError("Изменить город прибытия")
        qs = Train.objects.filter(
                                  travel_time=self.travel_time).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError("Измените время в пути")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
