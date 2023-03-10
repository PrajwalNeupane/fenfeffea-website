from django.db import models
from streams import blocks
from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.fields import StreamField

class Members(Page):

    template = "members/members.html"

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
        verbose_name = "Members Page"
        verbose_name_plural = "Members Pages"