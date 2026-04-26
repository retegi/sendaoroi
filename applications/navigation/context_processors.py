from django.db.models import Prefetch

from .models import MenuItem


def navbar_items(request):
    children_qs = MenuItem.objects.filter(is_active=True).order_by("order", "id")
    menu_items = (
        MenuItem.objects.filter(is_active=True, parent__isnull=True)
        .prefetch_related(Prefetch("children", queryset=children_qs))
        .order_by("order", "id")
    )
    return {"navbar_items": menu_items}
