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

list_urls = [
    path('counterparty/', CounterpartyListView.as_view()),
]

detail_urls = [
    path('counterparty/<int:pk>/', CounterpartyDetailView.as_view()),
]

urlpatterns = [
    path('list/', include(list_urls)),
    path('detail/', include(detail_urls)),
]


urlpatterns += router.urls
