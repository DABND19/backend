from django.db import models
from django.core.validators import RegexValidator


class Organisation(models.Model):
    """Здесь храним все организации"""
    name = models.CharField(
        max_length=256,
        unique=True
    )
    taxpayer_id = models.CharField(
        max_length=12,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'\d{12}',
                message='ИНН - последовательность из 12 цифр',
                code='invalid_taxpayer_id'
            )
        ]
    )


class Address(models.Model):
    """Здесь храним все адреса"""
    owner = models.ForeignKey(to=Organisation, on_delete=models.CASCADE)
    detail = models.CharField(max_length=256)


class LegalAddress(models.Model):
    """Здесь храним юридический адрес"""
    organisation = models.ForeignKey(
        to=Organisation,
        on_delete=models.CASCADE
    )
    address = models.OneToOneField(
        to=Address,
        on_delete=models.CASCADE
    )


class Contact(models.Model):
    """Здесь храним все контакты"""
    organisation = models.ForeignKey(
        to=Organisation,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=128, unique=True)
    phone = models.CharField(max_length=16, null=True)
    email = models.EmailField(null=True)


class LegalContact(models.Model):
    """Здесь храним контакты доверенных лиц организации"""
    organisation = models.ForeignKey(
        to=Organisation,
        on_delete=models.CASCADE
    )
    contact = models.OneToOneField(
        to=Contact,
        on_delete=models.CASCADE
    )
