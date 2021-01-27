from django.db import models
import mainbase.models as mainbase
from django.utils.translation import gettext as _


class Client(models.Model):
    organisation = models.OneToOneField(
        to=mainbase.Counterparty,
        on_delete=models.CASCADE,
        related_name='organisation_info'
    )

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Contact(mainbase.Contact):
    client = models.ForeignKey(
        verbose_name='Клиент',
        to=Client,
        on_delete=models.CASCADE,
        related_name='contacts'
    )

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class ActualAddress(mainbase.Address):
    client = models.ForeignKey(
        verbose_name='Клиент',
        to=Client,
        on_delete=models.CASCADE,
        related_name='actual_addresses'
    )

    class Meta:
        verbose_name = 'Физический адрес'
        verbose_name_plural = 'Физические адреса'


class Contract(models.Model):
    client = models.ForeignKey(
        verbose_name='Клиент',
        to=Client,
        on_delete=models.PROTECT,
        related_name='contracts'
    )
    category = models.CharField(
        verbose_name='Тип',
        max_length=8,
        choices=[
            ('CON', 'Контракт'),
            ('AGR', 'Договор'),
        ]
    )
    number = models.CharField(
        verbose_name='Номер',
        max_length=32
    )
    begin = models.DateField(
        verbose_name='Заключен'
    )
    end = models.DateField(
        verbose_name='Истекает'
    )

    class Meta:
        ordering = get_latest_by = ['end']
        verbose_name = 'Контракт/договор'
        verbose_name_plural = 'Контракты/договора'
        unique_together = ['category', 'number']


class Quarter(models.Model):
    year = models.PositiveSmallIntegerField(
        verbose_name='Год'
    )
    number = models.PositiveSmallIntegerField(
        verbose_name='Номер'
    )
    begin = models.DateField(
        verbose_name='Начало'
    )
    end = models.DateField(
        verbose_name='Конец'
    )

    class Meta:
        verbose_name = 'Квартал'
        verbose_name_plural = 'Кварталы'
        unique_together = ['year', 'number']
        ordering = get_latest_by = ['year', 'number']


class Protocol(models.Model):
    client = models.ForeignKey(
        verbose_name='Клиент',
        to=Client,
        on_delete=models.PROTECT,
        related_name='protocols'
    )
    quarter = models.ForeignKey(
        verbose_name='Квартал',
        to=Quarter,
        on_delete=models.CASCADE
    )
    number = models.CharField(
        verbose_name='Номер',
        max_length=16,
        unique=True
    )

    class Meta:
        verbose_name = 'Протокол'
        verbose_name_plural = 'Протоколы'


class Invoice(models.Model):
    client = models.ForeignKey(
        verbose_name='Клиент',
        to=Client,
        on_delete=models.PROTECT,
        related_name='invoices'
    )
    quarter = models.ForeignKey(
        verbose_name='Квартал',
        to=Quarter,
        on_delete=models.CASCADE
    )
    number = models.CharField(
        verbose_name='Номер',
        max_length=16,
        unique=True
    )
    is_returned = models.BooleanField(
        default=False,
        verbose_name='Статус'
    )
    returned_at = models.ForeignKey(
        null=True,
        verbose_name='Квартал возврата',
        to=Quarter,
        on_delete=models.CASCADE,
        related_name='returned_invoices'
    )
    total = models.PositiveIntegerField(
        verbose_name='Сумма'
    )

    class Meta:
        verbose_name = 'Счет/акт'
        verbose_name_plural = 'Счета/акты'


class TransmittedDocument(models.Model):
    client = models.ForeignKey(
        verbose_name='Клиент',
        to=Client,
        on_delete=models.PROTECT,
        related_name='transmitted_documents'
    )
    quarter = models.ForeignKey(
        verbose_name='Квартал',
        to=Quarter,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name='Наименование',
        max_length=128
    )
    is_returned = models.BooleanField(
        verbose_name='Статус'
    )

    class Meta:
        verbose_name = 'Переданный документ'
        verbose_name_plural = 'Переданные документы'
