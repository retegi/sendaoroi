from django.urls import path

from .views import EditablePageDetailView

app_name = "pages"

urlpatterns = [
    path("paginas/<slug:slug>/", EditablePageDetailView.as_view(), name="detail"),
]
