from django.db import models
from wagtail.models import Page 
from wagtail.admin.edit_handlers import FieldPanel

class ContactForm(Page):
    template = 'contact/contact.html'

    logo_image = models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content_panels = Page.content_panels + [
        FieldPanel('logo_image'),
    ]

    class Meta:
        verbose_name = 'contact-form'
        verbose_name_plural = 'contact-forms'
