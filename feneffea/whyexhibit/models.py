from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


# Create your models here.
class WhyExhibit(Page):
    template = "whyexhibit/whyexhibit.html"

    image1 = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    image2 = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    image3 = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    image4 = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    image5 = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    image6 = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    logo_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel("logo_image"),
        FieldPanel("image1"),
        FieldPanel("image2"),
        FieldPanel("image3"),
        FieldPanel("image4"),
        FieldPanel("image5"),
        FieldPanel("image6"),
    ]

    class Meta:
        verbose_name = "WhyExhibit"
        verbose_name_plural = "WhyExhibits"
