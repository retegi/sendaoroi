from django.db import models
from django.utils.translation import gettext_lazy as _


class MenuItem(models.Model):
    ITEM_TYPE_PAGE = "page"
    ITEM_TYPE_INTERNAL_URL = "internal_url"
    ITEM_TYPE_ANCHOR = "anchor"
    ITEM_TYPE_EXTERNAL_URL = "external_url"

    ITEM_TYPES = (
        (ITEM_TYPE_PAGE, _("Page")),
        (ITEM_TYPE_INTERNAL_URL, _("Internal URL")),
        (ITEM_TYPE_ANCHOR, _("Anchor")),
        (ITEM_TYPE_EXTERNAL_URL, _("External URL")),
    )

    title = models.CharField(max_length=255)
    item_type = models.CharField(max_length=20, choices=ITEM_TYPES, default=ITEM_TYPE_PAGE)
    page = models.ForeignKey(
        "pages.EditablePage",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="menu_items",
    )
    url = models.CharField(max_length=500, blank=True)
    anchor = models.CharField(max_length=255, blank=True)

    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children",
    )

    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    open_in_new_tab = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Menu item")
        verbose_name_plural = _("Menu items")
        ordering = ("order", "id")

    def __str__(self) -> str:
        return self.title

    def get_url(self):
        if self.item_type == self.ITEM_TYPE_PAGE and self.page:
            return self.page.get_absolute_url()
        if self.item_type == self.ITEM_TYPE_ANCHOR:
            return self.anchor or "#"
        if self.item_type in {self.ITEM_TYPE_INTERNAL_URL, self.ITEM_TYPE_EXTERNAL_URL}:
            return self.url or "#"
        return "#"

    @property
    def has_active_children(self):
        return self.children.filter(is_active=True).exists()
