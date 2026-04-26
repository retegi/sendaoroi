from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import HomeContent


@admin.register(HomeContent)
class HomeContentAdmin(TranslationAdmin):
    list_display = ("hero_title", "is_active", "updated_at")
    list_filter = ("is_active", "updated_at")
    search_fields = ("hero_title", "intro_title", "services_title")
    readonly_fields = ("updated_at",)
    fieldsets = (
        ("Hero", {"fields": ("hero_title", "hero_subtitle", "hero_text", "hero_image")}),
        ("Intro", {"fields": ("intro_title", "intro_text")}),
        ("Process", {"fields": ("process_title", "process_text", "process_image")}),
        ("Services", {"fields": ("services_title", "services_text")}),
        ("Team", {"fields": ("team_title", "team_text")}),
        ("FAQ", {"fields": ("faq_title", "faq_text")}),
        ("Contact", {"fields": ("contact_title", "contact_text")}),
        ("SEO", {"fields": ("seo_title", "seo_description")}),
        ("State", {"fields": ("is_active", "updated_at")}),
    )
