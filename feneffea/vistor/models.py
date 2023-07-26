from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class Visitor(Page):
    template = "visitor/visitor.html"

    logo_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    visitor_img = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel("logo_image"),
        FieldPanel("visitor_img"),
    ]

    class Meta:
        verbose_name = "visitor"
        verbose_name_plural = "visitors"


# Create your models here.
