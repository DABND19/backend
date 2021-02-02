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
    
]

detail_urls = [
    path('client/<int:pk>/', ClientDetailView.as_view()),
]

urlpatterns = [
    path('client/list/', ClientListView.as_view()),
    path('contract/list/', ContractListView.as_view()),
    path('invoice/list/', InvoiceListView.as_view()),
    path('client/detail/<int:pk>/', ClientDetailView.as_view()),
]


urlpatterns += router.urls
