from django.db import models
from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from streams import blocks
from wagtail.fields import StreamField

# Create your models here.
class Publication(Page):
    template = 'publication/publication.html'

    logo_image = models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    content = StreamField(
        [
        ("pubs", blocks.Pubs())
        ],
        null = True,
        blank = True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('logo_image'),
        FieldPanel('content'),
    ]

    class Meta:
        verbose_name = 'publication'
        verbose_name_plural = 'publications'