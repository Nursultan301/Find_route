from django.db import models


class Route(models.Model):
    name = models.CharField("Называние маршрута", max_length=50, unique=True)
    travel_times = models.PositiveSmallIntegerField("Общее время в пути")
    from_city = models.ForeignKey("cities.City", on_delete=models.CASCADE,
                                  related_name='route_from_city_set',
                                  verbose_name='Из какого города')
    to_city = models.ForeignKey("cities.City", on_delete=models.CASCADE,
                                related_name='route_to_city_set',
                                verbose_name="В какой город")
    trains = models.ManyToManyField('trains.Train', verbose_name="Список поездов")

    objects = models.Manager()

    class Meta:
        verbose_name = "Маршурт"
        verbose_name_plural = "Маршурты"
        ordering = ['travel_times']

    def __str__(self):
        return f'Маршурт {self.name} из города {self.from_city}'


