from django.db import models
from .client import Client
from mainbase.models import Contact as MainContact


class Contact(MainContact):
    client = models.ForeignKey(
        verbose_name='Клиент',
        to=Client,
        on_delete=models.CASCADE,
        related_name='contacts'
    )

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
