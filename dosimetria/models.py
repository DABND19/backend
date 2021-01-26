from django.db import models
import main.models as main


class Client(models.Model):
    """
    ИДК клиент
    """
    organisation = models.ForeignKey(
        to=main.Organisation,
        on_delete=models.CASCADE
    )

    is_work_in_progress = models.BooleanField(default=True)

    DTU_num = models.PositiveSmallIntegerField(default=0)
    DTL_num = models.PositiveSmallIntegerField(default=0)


class Address(models.Model):
    """
    Адрес ИДК клиента
    """
    organisation = models.ForeignKey(
        to=Client,
        on_delete=models.CASCADE
    )
    address = models.OneToOneField(
        to=main.Address,
        on_delete=models.PROTECT
    )


class Contract(models.Model):
    """
    Контактная информация ИДК клиента
    """
    organisation = models.ForeignKey(to=Client, on_delete=models.PROTECT)
    number = models.CharField(max_length=32)
    begin = models.DateField()
    end = models.DateField()


class Quarter(models.Model):
    """
    Квартальная отчетность
    """
    year = models.PositiveSmallIntegerField()
    number = models.PositiveSmallIntegerField()

    begin = models.DateField()
    end = models.DateField()

    total = models.PositiveBigIntegerField(null=True)


class Protocol(models.Model):
    """
    Протокол проведенных работ с ИДК клиентом
    """
    organisation = models.ForeignKey(
        to=Client,
        on_delete=models.PROTECT
    )
    quarter = models.ForeignKey(
        to=Quarter,
        on_delete=models.PROTECT
    )

    number = models.CharField(max_length=32)


class Document(models.Model):
    """
    Документ, переданный клиенту в определенный квартал
    """
    organisation = models.ForeignKey(
        to=Client,
        on_delete=models.PROTECT
    )
    quarter = models.ForeignKey(
        to=Quarter,
        on_delete=models.PROTECT
    )

    name = models.CharField(max_length=256)
    is_returned = models.BooleanField(default=False)


class Invoice(models.Model):
    """
    Счет, выставленный ИДК клиенту в определенный квартал
    """
    organisation = models.ForeignKey(
        to=Client,
        on_delete=models.PROTECT
    )
    quarter = models.ForeignKey(
        to=Quarter,
        on_delete=models.PROTECT,
        related_name='issued_at'
    )

    number = models.CharField(max_length=32)
    total = models.PositiveIntegerField()
    returned_at = models.ForeignKey(
        to=Quarter, 
        on_delete=models.PROTECT,
        related_name='returned_at'
    )
    is_returned = models.BooleanField(default=False)
