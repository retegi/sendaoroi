from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from .models import EditablePage


class EditablePageDetailView(DetailView):
    template_name = "pages/detail.html"
    context_object_name = "page"

    def get_object(self, queryset=None):
        return get_object_or_404(EditablePage.objects.filter(is_active=True), slug=self.kwargs["slug"])
