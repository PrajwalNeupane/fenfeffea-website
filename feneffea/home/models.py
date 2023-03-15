from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.fields import StreamField
from streams import blocks
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images.models import Image


class HomePage(Page):
    """ home page model. """
    templates = "home/home_page.html"
    max_count = 1

    content = StreamField(
        [
        ("event_listings", blocks.Cards())
        ],
        null = True,
        blank = True,
    )

    carousal_text1 = models.CharField(max_length=100, blank=False, null=True)
    carousal_text2 = models.CharField(max_length=100, blank=False, null=True)
    carousal_text3 = models.CharField(max_length=100, blank=False, null=True)
    home_message_header = models.CharField(max_length=100, blank=False, null=True)
    home_message_content = RichTextField()

    logo_image = models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    jumbotron_img = models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    carousal1 = models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    carousal2 = models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    carousal3 = models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    home_message_img = models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content_panels = Page.content_panels + [
        FieldPanel("logo_image"),
        FieldPanel("jumbotron_img"),
        FieldPanel("carousal1"),
        FieldPanel("carousal_text1"),
        FieldPanel("carousal2"),
        FieldPanel("carousal_text2"),
        FieldPanel("carousal3"),
        FieldPanel("carousal_text3"),
        PageChooserPanel("banner_cta"),
        FieldPanel("home_message_img"),
        FieldPanel("home_message_header"),
        FieldPanel("home_message_content"),
        FieldPanel("content")
    ]

    class Meta:

        verbose_name = "Home Pages"
        verbose_name_plural = 'Home Pages'
