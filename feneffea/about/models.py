from django.db import models
from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.fields import StreamField
from streams import blocks

class About(Page):

    template = "about/about.html"

    content = StreamField(
        [
        ("board_members", blocks.Cards())
        ],
        null = True,
        blank = True,
    )

    logo_image = models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )


    content_panels = Page.content_panels + [
        FieldPanel("logo_image"),
        FieldPanel("content"),
    ]

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Pages"
