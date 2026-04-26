from django.db import models
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = HTMLField()
    category = models.CharField(max_length=120, blank=True)
    order = models.PositiveIntegerField(default=0)

    show_on_home = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQs")
        ordering = ("order", "id")

    def __str__(self) -> str:
        return self.question
