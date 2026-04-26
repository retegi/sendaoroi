from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Collaborator


class CollaboratorListView(ListView):
    template_name = "team/list.html"
    context_object_name = "collaborators"

    def get_queryset(self):
        queryset = Collaborator.objects.filter(is_active=True).order_by("order", "name")
        collaborator_type = self.request.GET.get("type")
        membership_type = self.request.GET.get("membership")

        if collaborator_type in {Collaborator.TYPE_PERSON, Collaborator.TYPE_ENTITY}:
            queryset = queryset.filter(collaborator_type=collaborator_type)
        if membership_type in {Collaborator.MEMBERSHIP_OWN, Collaborator.MEMBERSHIP_EXTERNAL}:
            queryset = queryset.filter(membership_type=membership_type)

        return queryset


class CollaboratorDetailView(DetailView):
    template_name = "team/detail.html"
    context_object_name = "collaborator"

    def get_object(self, queryset=None):
        return get_object_or_404(Collaborator.objects.filter(is_active=True), slug=self.kwargs["slug"])
