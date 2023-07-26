from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
)
from wagtail.fields import RichTextField

from modelcluster.fields import ParentalKey
from wagtail.contrib.forms.models import AbstractFormField, AbstractEmailForm
from wagtailcaptcha.models import WagtailCaptchaEmailForm


class FormField(AbstractFormField):
    page = ParentalKey(
        "RegistrationPage",
        on_delete=models.CASCADE,
        related_name="form_fields",
    )


class RegistrationPage(AbstractEmailForm):
    template = "registration/registration.html"

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    logo_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    registration_img = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel("logo_image"),
        FieldPanel("registration_img"),
        FieldPanel("intro"),
        InlinePanel("form_fields", label="Form Fields"),
        FieldPanel("thank_you_text"),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("from_address", classname="col6"),
                        FieldPanel("to_address", classname="col6"),
                    ]
                ),
                FieldPanel("subject"),
            ],
            heading="Email Settings",
        ),
    ]

    class Meta:
        verbose_name = "registration"
        verbose_name_plural = "registrations"
