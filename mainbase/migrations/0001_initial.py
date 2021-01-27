# Generated by Django 3.1.5 on 2021-01-27 13:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postcode', models.PositiveSmallIntegerField(verbose_name='Почтовый индекс')),
                ('region', models.CharField(max_length=64, verbose_name='Регион')),
                ('area', models.CharField(max_length=64, verbose_name='Район')),
                ('city', models.CharField(max_length=64, verbose_name='Населенный пункт')),
                ('street', models.CharField(max_length=64, verbose_name='Улица')),
                ('building', models.CharField(max_length=8, verbose_name='Дом/строение')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=32, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=32, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=32, verbose_name='Отчество')),
                ('phone', models.CharField(max_length=16, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
            ],
        ),
        migrations.CreateModel(
            name='Counterparty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='Наименование')),
                ('taxpayer_id', models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator(message='ИНН - последовательность 12 цифр', regex='\\d{12}')], verbose_name='ИНН')),
            ],
            options={
                'verbose_name': 'Контрагент',
                'verbose_name_plural': 'Контрагенты',
            },
        ),
        migrations.CreateModel(
            name='LegalContact',
            fields=[
                ('contact_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mainbase.contact')),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='legal_contacts', to='mainbase.counterparty', verbose_name='Организация')),
            ],
            options={
                'verbose_name': 'Доверенное лицо',
                'verbose_name_plural': 'Доверенные лица',
            },
            bases=('mainbase.contact',),
        ),
        migrations.CreateModel(
            name='ActualAddress',
            fields=[
                ('address_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mainbase.address')),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actual_addresses', to='mainbase.counterparty', verbose_name='Организация')),
            ],
            options={
                'verbose_name': 'Физический адрес',
                'verbose_name_plural': 'Физические адреса',
            },
            bases=('mainbase.address',),
        ),
    ]
