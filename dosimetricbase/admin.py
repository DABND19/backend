from django.contrib import admin

from dosimetricbase.models import (
    ActualAddress,
    Client,
    Contact,
    Contract,
    Invoice,
    Protocol,
    Quarter,
    TransmittedDocument
)

admin.register(ActualAddress)
admin.register(Client)
admin.register(Contact)
admin.register(Contract)
admin.register(Invoice)
admin.register(Protocol)
admin.register(Quarter)
admin.register(TransmittedDocument)
