from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls.jwt')),
    path('main/', include('mainbase.urls')),
    path('dosimetria/', include('dosimetricbase.urls'))
]
