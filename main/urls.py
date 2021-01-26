from rest_framework.routers import DefaultRouter

from main.api.models import (
    OrganisationAPI,
    AddressAPI,
    LegalAddressAPI,
    ContactAPI,
    LegalContactAPI
)

from main.api.details import (
    OrganisationDetailView
)


router = DefaultRouter()

# API для моделей
# router.register('organisation', OrganisationAPI)
router.register('address', AddressAPI)
router.register('legal-address', LegalAddressAPI)
router.register('contact', ContactAPI)
router.register('legal-contact', LegalContactAPI)

# API для представлений
router.register('organisation-detail', OrganisationDetailView)


urlpatterns = router.urls
