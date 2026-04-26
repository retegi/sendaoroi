from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import FAQ


@admin.register(FAQ)
class FAQAdmin(TranslationAdmin):
    list_display = ("question", "category", "order", "show_on_home", "is_active")
    list_filter = ("is_active", "show_on_home", "category", "created_at")
    search_fields = ("question", "answer", "category")
    ordering = ("order", "id")
