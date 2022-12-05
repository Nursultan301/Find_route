from django.core.exceptions import ValidationError
from django.db import models


class Train(models.Model):
    title = models.CharField("Номер поезда", max_length=50, unique=True)
    travel_time = models.PositiveSmallIntegerField("Время в пути")
    from_city = models.ForeignKey("cities.City", on_delete=models.CASCADE,
                                  related_name='from_city_set', verbose_name="Из какого города")
    to_city = models.ForeignKey("cities.City", on_delete=models.CASCADE,
                                related_name='to_city_set', verbose_name="В какой город")

    def __str__(self):
        return f'Поезд №{self.title} из города  {self.from_city}'

    def clean(self):
        try:
            if self.from_city.id == self.to_city.id:
                raise ValidationError('Изменить город прибытия')
            qs = Train.objects.filter(from_city=self.from_city, to_city=self.to_city,
                                      travel_time=self.travel_time).exclude(pk=self.pk)
            if qs.exists():
                raise ValidationError('Измените время в пути')
        except (Train.from_city.RelatedObjectDoesNotExist, Train.to_city.RelatedObjectDoesNotExist):
            raise ValidationError('Обязательное поле')

    def save(self, *args, **kwargs):
        self.clean()
        super(Train, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Поезд'
        verbose_name_plural = 'Поезда'
        ordering = ['travel_time']
