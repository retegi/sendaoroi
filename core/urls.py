from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("rosetta/", include("rosetta.urls")),
    path("i18n/", include("django.conf.urls.i18n")),
    path("tinymce/", include("tinymce.urls")),
    path("accounts/", include("allauth.urls")),
]

urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    path("", include("applications.home.urls")),
    path("", include("applications.pages.urls")),
    path("", include("applications.team.urls")),
    path("", include("applications.faq.urls")),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
