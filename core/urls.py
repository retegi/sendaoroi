from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path("rosetta/", include("rosetta.urls")),
    path("i18n/", include("django.conf.urls.i18n")),  # 👈 ESTA LÍNEA FALTABA
]

urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    path("", include("applications.home.urls")),
)