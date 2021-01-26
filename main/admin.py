from django.contrib import admin
from main.models import (
    Organisation,
    Address,
    LegalAddress,
    Contact,
    LegalContact
)

# Register your models here.
admin.register(Organisation)
admin.register(Address)
admin.register(LegalAddress)
admin.register(Contact)
admin.register(LegalContact)

