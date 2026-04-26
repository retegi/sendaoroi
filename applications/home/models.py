from django.db import models
from django.utils.translation import gettext_lazy as _


class HomeContent(models.Model):
    hero_title = models.CharField(max_length=255, blank=True)
    hero_subtitle = models.CharField(max_length=255, blank=True)
    hero_text = models.TextField(blank=True)
    hero_image = models.ImageField(upload_to="home/", blank=True, null=True)

    intro_title = models.CharField(max_length=255, blank=True)
    intro_text = models.TextField(blank=True)

    process_title = models.CharField(max_length=255, blank=True)
    process_text = models.TextField(blank=True)
    process_image = models.ImageField(upload_to="home/", blank=True, null=True)

    services_title = models.CharField(max_length=255, blank=True)
    services_text = models.TextField(blank=True)

    team_title = models.CharField(max_length=255, blank=True)
    team_text = models.TextField(blank=True)

    faq_title = models.CharField(max_length=255, blank=True)
    faq_text = models.TextField(blank=True)

    contact_title = models.CharField(max_length=255, blank=True)
    contact_text = models.TextField(blank=True)

    seo_title = models.CharField(max_length=255, blank=True)
    seo_description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Home content")
        verbose_name_plural = _("Home content")

    def __str__(self) -> str:
        return self.hero_title or _("Home content")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.is_active:
            HomeContent.objects.exclude(pk=self.pk).update(is_active=False)

    @classmethod
    def get_active(cls):
        return cls.objects.filter(is_active=True).first() or cls.objects.order_by("id").first()
