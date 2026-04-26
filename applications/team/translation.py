from modeltranslation.translator import TranslationOptions, register

from .models import Collaborator


@register(Collaborator)
class CollaboratorTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "role",
        "short_description",
        "full_description",
    )
