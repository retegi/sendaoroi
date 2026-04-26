from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import EditablePage


@admin.register(EditablePage)
class EditablePageAdmin(TranslationAdmin):
    list_display = ("title", "slug", "parent", "menu_group", "order", "is_active", "updated_at")
    list_filter = ("is_active", "menu_group", "created_at", "updated_at")
    search_fields = ("title", "slug", "summary", "content")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("order", "title")
