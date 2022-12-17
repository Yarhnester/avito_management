# Generated by Django 3.2.16 on 2022-12-17 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pvz', models.CharField(blank=True, choices=[('PVZ1', 'ПВЗ-1'), ('PVZ2', 'ПВЗ-2'), ('PVZ3', 'ПВЗ-3'), ('PVZ4', 'ПВЗ-4'), ('PVZ5', 'ПВЗ-5'), ('PVZ6', 'ПВЗ-6'), ('PVZ7', 'ПВЗ-7'), ('PVZ8', 'ПВЗ-8')], default=None, max_length=4, verbose_name='ПВЗ')),
                ('service', models.CharField(blank=True, max_length=50, verbose_name='Услуга')),
                ('partner', models.CharField(blank=True, max_length=150, verbose_name='Контрагент')),
                ('contact', models.CharField(blank=True, max_length=150, verbose_name='Контактное лицо')),
                ('the_original_contract', models.CharField(blank=True, choices=[('Original', 'Оригинал'), ('Copy', 'Копия'), ('Absent', 'Отсутствует'), ('Not needed', 'Не нужен')], default='Not needed', max_length=10, verbose_name='Статус договора')),
                ('rate', models.IntegerField(blank=True, verbose_name='Тариф')),
                ('payment_date', models.DateField(verbose_name='Дата оплаты')),
                ('document', models.CharField(blank=True, max_length=150, verbose_name='Доставка документов')),
                ('edo', models.CharField(blank=True, choices=[('Yes', 'Да'), ('No', 'Нет')], default='No', max_length=3, verbose_name='ЭДО')),
                ('notes', models.TextField(blank=True, max_length=250, verbose_name='Примечания')),
            ],
            options={
                'verbose_name': 'Договор',
                'verbose_name_plural': 'Договора',
            },
        ),
    ]
