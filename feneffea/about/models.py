from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField, RichTextField
from streams import blocks


class About(Page):
    template = "about/about.html"
    content = StreamField(
        [("board_members", blocks.Cards())],
        null=True,
        blank=True,
    )

    accordion = StreamField(
        [("accordian", blocks.BoardHistoryAccordion())],
        null=True,
        blank=True,
    )

    accordion = StreamField(
        [("Board_History_Accordion", blocks.BoardHistoryAccordion())],
        null=True,
        blank=True,
    )

    home_message_content = RichTextField(null=True)
    about_feneffea = RichTextField(null=True)

    logo_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    home_message_img = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel("logo_image"),
        FieldPanel("home_message_content"),
        FieldPanel("home_message_img"),
        FieldPanel("about_feneffea"),
        FieldPanel("content"),
        FieldPanel("accordion"),
    ]

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Pages"
