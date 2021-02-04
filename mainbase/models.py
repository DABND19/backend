from django.db import models
from django.core.validators import RegexValidator


class Counterparty(models.Model):
    name = models.CharField(
        verbose_name='Наименование',
        max_length=256,
        unique=True
    )
    taxpayer_id = models.CharField(
        verbose_name='ИНН',
        max_length=12,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'\d{12}',
                message='ИНН - последовательность 12 цифр'
            )
        ]
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'


class Contact(models.Model):
    surname = models.CharField(
        verbose_name='Фамилия',
        max_length=32
    )
    name = models.CharField(
        verbose_name='Имя',
        max_length=32
    )
    patronymic = models.CharField(
        verbose_name='Отчество',
        max_length=32
    )
    phone = models.CharField(
        verbose_name='Номер телефона',
        max_length=16
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
    )

    def fullname(self):
        return ' '.join([
            self.surname, 
            self.name, 
            self.patronymic
        ])

    class Meta:
        abstract = True


class LegalContact(Contact):
    organisation = models.ForeignKey(
        verbose_name='Организация',
        to=Counterparty,
        on_delete=models.CASCADE,
        related_name='legal_contacts'
    )

    class Meta:
        verbose_name = 'Доверенное лицо'
        verbose_name_plural = 'Доверенные лица'


class Address(models.Model):
    postcode = models.PositiveSmallIntegerField(
        verbose_name='Почтовый индекс'
    )
    region = models.CharField(
        verbose_name='Регион',
        max_length=64
    )
    area = models.CharField(
        max_length=64,
        verbose_name='Район'
    )
    city = models.CharField(
        max_length=64,
        verbose_name='Населенный пункт'
    )
    street = models.CharField(
        max_length=64,
        verbose_name='Улица'
    )
    building = models.CharField(
        max_length=8,
        verbose_name='Дом/строение'
    )

    def full(self):
        return f'{self.postcode}, {self.region}, {self.area}, {self.city}, {self.street}, {self.building}'

    def __str__(self):
        return self.full()

    class Meta:
        abstract = True


class ActualAddress(Address):
    organisation = models.ForeignKey(
        verbose_name='Организация',
        to=Counterparty,
        on_delete=models.CASCADE,
        related_name='actual_addresses'
    )

    class Meta:
        verbose_name = 'Физический адрес'
        verbose_name_plural = 'Физические адреса'
