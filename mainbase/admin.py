from django.contrib import admin

from mainbase.models import (
    Counterparty,
    ActualAddress,
    LegalContact
)


admin.register(Counterparty)
admin.register(ActualAddress)
admin.register(LegalContact)
