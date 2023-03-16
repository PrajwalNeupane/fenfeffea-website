from django.db import models
from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel

class Registrations(Page):
    template = 'registration/registration.html'

    logo_image = models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    registration_img = models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content_panels = Page.content_panels + [
        FieldPanel('logo_image'),
        FieldPanel('registration_img'),
    ]
    
    class Meta:
        verbose_name = 'registration'
        verbose_name_plural = 'registrations'

