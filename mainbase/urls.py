from django.urls import path
from rest_framework.routers import DefaultRouter

from mainbase.api import (
    ActualAddressAPI,
    LegalContactAPI,
    CounterpartyListAPI,
    CounterpartyRetrieveAPI
)

router = DefaultRouter()

router.register('legal-contact', LegalContactAPI)
router.register('actual-address', ActualAddressAPI)

urlpatterns = [
    path('counterparty/', CounterpartyListAPI.as_view()),
    path('counterparty/<int:pk>', CounterpartyRetrieveAPI.as_view())
]

urlpatterns += router.urls
