from django.urls import path, include
from rest_framework.routers import DefaultRouter

from dosimetricbase.api import (
    ActualAddressAPI,
    ClientAPI,
    ContactAPI,
    ContractAPI,
    InvoiceAPI,
    ProtocolAPI,
    QuarterAPI,
    TransmittedDocumentAPI
)

from dosimetricbase.views import (
    ClientDetailView,
    ClientListView,
    ContractListView,
    InvoiceListView
)

router = DefaultRouter()

router.register('actual-address', ActualAddressAPI)
router.register('client', ClientAPI)
router.register('contact', ContactAPI)
router.register('contract', ContractAPI)
router.register('invoice', InvoiceAPI)
router.register('protocol', ProtocolAPI)
router.register('quarter', QuarterAPI)
router.register('transmitted-document', TransmittedDocumentAPI)

list_urls = [
    path('client/', ClientListView.as_view()),
    path('contract/', ContractListView.as_view()),
    path('invoice/', InvoiceListView.as_view()),
]

detail_urls = [
    path('client/<int:pk>/', ClientDetailView.as_view()),
]

urlpatterns = [
    path('list/', include(list_urls)),
    path('detail/', include(detail_urls)),
]


urlpatterns += router.urls
