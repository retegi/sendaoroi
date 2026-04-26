from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(TranslationAdmin):
    list_display = ("title", "item_type", "parent", "order", "is_active", "open_in_new_tab")
    list_filter = ("item_type", "is_active", "open_in_new_tab", "created_at", "updated_at")
    search_fields = ("title", "url", "anchor")
    ordering = ("parent__id", "order", "id")
