from django.urls import path, include
from rest_framework.routers import DefaultRouter

from mainbase.api import (
    ActualAddressAPI,
    CounterpartyAPI,
    LegalContactAPI
)

from mainbase.views import (
    CounterpartyDetailView,
    CounterpartyListView
)

router = DefaultRouter()

router.register('legal-contact', LegalContactAPI)
router.register('actual-address', ActualAddressAPI)
router.register('counterparty', CounterpartyAPI)

urlpatterns = [
    path('counterparty/list/', CounterpartyListView.as_view()),
    path('counterparty/detail/<int:pk>/', CounterpartyDetailView.as_view()),
]


urlpatterns += router.urls
