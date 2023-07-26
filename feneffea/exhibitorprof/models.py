from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class ExhibitorProf(Page):
    template = "exhibitorprof/exhibitorproj.html"

    logo_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    wood_img = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel("logo_image"),
        FieldPanel("wood_img"),
    ]

    class Meta:
        verbose_name = "ExhibitorsProf"
        verbose_name_plural = "ExhibitorsProfs"
