from modeltranslation.translator import TranslationOptions, register

from .models import HomeContent


@register(HomeContent)
class HomeContentTranslationOptions(TranslationOptions):
    fields = (
        "hero_title",
        "hero_subtitle",
        "hero_text",
        "intro_title",
        "intro_text",
        "process_title",
        "process_text",
        "services_title",
        "services_text",
        "team_title",
        "team_text",
        "faq_title",
        "faq_text",
        "contact_title",
        "contact_text",
        "seo_title",
        "seo_description",
    )
