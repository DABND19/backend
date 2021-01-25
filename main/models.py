from django.db import models
from django.core.validators import RegexValidator


class Сounterparty(models.Model):
    name = models.CharField(max_length=256)
    taxpayer_id = models.CharField(
        max_length=12, 
        validators=[
            RegexValidator(
                regex=r'\d{12}',
                message='ИНН - последовательность из 12 цифр',
                code='invalid_taxpayer_id'
            )
        ]
    )
