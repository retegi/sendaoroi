from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField


class EditablePage(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    summary = models.TextField(blank=True)
    content = HTMLField(blank=True)
    featured_image = models.ImageField(upload_to="pages/", blank=True, null=True)

    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children",
    )
    menu_group = models.CharField(max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    seo_title = models.CharField(max_length=255, blank=True)
    seo_description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Editable page")
        verbose_name_plural = _("Editable pages")
        ordering = ("order", "title")

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("pages:detail", kwargs={"slug": self.slug})
