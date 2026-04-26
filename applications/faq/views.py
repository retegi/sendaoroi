from django.views.generic import ListView

from .models import FAQ


class FAQListView(ListView):
    template_name = "faq/list.html"
    context_object_name = "faqs"

    def get_queryset(self):
        return FAQ.objects.filter(is_active=True).order_by("order", "id")
