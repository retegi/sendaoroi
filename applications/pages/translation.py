from modeltranslation.translator import TranslationOptions, register

from .models import EditablePage


@register(EditablePage)
class EditablePageTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "summary",
        "content",
        "seo_title",
        "seo_description",
        "menu_group",
    )
