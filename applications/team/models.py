from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField


class Collaborator(models.Model):
    TYPE_PERSON = "person"
    TYPE_ENTITY = "entity"
    TYPES = (
        (TYPE_PERSON, _("Person")),
        (TYPE_ENTITY, _("Entity")),
    )

    MEMBERSHIP_OWN = "own_member"
    MEMBERSHIP_EXTERNAL = "external_member"
    MEMBERSHIP_TYPES = (
        (MEMBERSHIP_OWN, _("Own member")),
        (MEMBERSHIP_EXTERNAL, _("External member")),
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    collaborator_type = models.CharField(max_length=20, choices=TYPES, default=TYPE_PERSON)
    membership_type = models.CharField(max_length=20, choices=MEMBERSHIP_TYPES, default=MEMBERSHIP_OWN)

    role = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to="team/", blank=True, null=True)
    short_description = models.TextField(blank=True)
    full_description = HTMLField(blank=True)

    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=100, blank=True)
    website_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    x_url = models.URLField(blank=True)

    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Collaborator")
        verbose_name_plural = _("Collaborators")
        ordering = ("order", "name")

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("team:detail", kwargs={"slug": self.slug})
