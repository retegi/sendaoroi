from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Collaborator


@admin.register(Collaborator)
class CollaboratorAdmin(TranslationAdmin):
    list_display = ("name", "collaborator_type", "membership_type", "order", "is_active")
    list_filter = ("collaborator_type", "membership_type", "is_active", "created_at")
    search_fields = ("name", "slug", "role", "short_description", "full_description")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("order", "name")
