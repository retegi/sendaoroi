from django.urls import path

from .views import CollaboratorDetailView, CollaboratorListView

app_name = "team"

urlpatterns = [
    path("grupo-de-trabajo/", CollaboratorListView.as_view(), name="list"),
    path("grupo-de-trabajo/<slug:slug>/", CollaboratorDetailView.as_view(), name="detail"),
]
