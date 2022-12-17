from django.db import models
from django.contrib.auth import get_user_model
from datetime import date

from core.context_processors.pvz_list import PVZ

User = get_user_model()


class Chart(models.Model):
    class Meta:
        verbose_name = 'График'
        verbose_name_plural = 'Графики'

    name = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='charts', verbose_name='Имя работника')
    date = models.DateField(default=date.today())
    hours = models.IntegerField(null=False)
    pvz = models.CharField(max_length=4, choices=PVZ, default=None, blank=True,
                           verbose_name='ПВЗ')
