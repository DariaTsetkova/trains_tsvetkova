from django.db import models


class Train(models.Model):
    number = models.IntegerField(verbose_name="Номер поезда")
    train_type = models.TextField(null=True, blank=True, verbose_name="Тип поезда")
    vagon_number = models.IntegerField(verbose_name="Количество вагонов")

    def __int__(self):
        return self.number

    class Meta:
        verbose_name_plural = 'Поезда'
        verbose_name = 'Поезд'
        ordering = ['number']


class Station(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    zone = models.TextField(null=True, blank=True, verbose_name="Тарифная зона")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Станции'
        verbose_name = 'Станция'
        ordering = ['name']


class Path(models.Model):
    start_station = models.ForeignKey('Station', null=True, on_delete=models.PROTECT, verbose_name='Начальная станция')
    end_station = models.ForeignKey('Station', null=True, on_delete=models.PROTECT, verbose_name='Конечная станция')
    station_list = models.TextField(null=True, blank=True, verbose_name="Список станций")
    start_time = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Отправление")
    end_time = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Прибытие")
    end_station = models.ForeignKey('Train', null=True, on_delete=models.PROTECT, verbose_name='Поезд')

    class Meta:
        verbose_name_plural = 'График движения'
        verbose_name = 'График движения'
        ordering = ['-id']
