from django.db import models


class Train(models.Model):
    name = models.CharField("Номер поезда", max_length=50, unique=True)
    travel_time = models.PositiveSmallIntegerField("Время в пути")
    from_city = models.ForeignKey("cities.City", on_delete=models.CASCADE,
                                  related_name='from_city_set',
                                  verbose_name='Из какого города')
    to_city = models.ForeignKey("cities.City", on_delete=models.CASCADE,
                                related_name='to_city_set',
                                verbose_name="В какой город")

    class Meta:
        verbose_name = "Поезд"
        verbose_name_plural = "Поезда"
        ordering = ['travel_time']

    def __str__(self):
        return f'Поезд №{self.name} из города {self.from_city}'
