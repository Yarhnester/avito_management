from django.db import models
from django.contrib.auth import get_user_model

from core.context_processors.pvz_list import PVZ

User = get_user_model()

Y_OR_N = (
    ('Yes', 'Да'),
    ('No', 'Нет')
)
status_contract = (
    ('Original', 'Оригинал'),
    ('Copy', 'Копия'),
    ('Absent', 'Отсутствует'),
    ('Not needed', 'Не нужен'),
)


class Record(models.Model):
    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договора'

    pvz = models.CharField(max_length=4, choices=PVZ, default=None, blank=True,
                           verbose_name='ПВЗ')
    service = models.CharField(max_length=50, blank=True, verbose_name='Услуга')
    partner = models.CharField(max_length=150, verbose_name='Контрагент',
                               blank=True)
    contact = models.CharField(max_length=150, verbose_name='Контактное лицо',
                               blank=True)
    the_original_contract = models.CharField(max_length=10, choices=status_contract,
                                             default='Not needed', blank=True,
                                             verbose_name='Статус договора')
    rate = models.IntegerField(blank=True, verbose_name='Тариф')
    payment_date = models.DateField(auto_now_add=False, verbose_name='Дата оплаты')
    document = models.CharField(max_length=150, blank=True,
                                verbose_name='Доставка документов')
    edo = models.CharField(max_length=3, choices=Y_OR_N, default='No',
                           blank=True, verbose_name='ЭДО')
    notes = models.TextField(max_length=250, blank=True, verbose_name='Примечания')
