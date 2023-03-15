from wagtail import blocks 
from wagtail.images.blocks import ImageChooserBlock


class Cards(blocks.StructBlock):

    card_group_title = blocks.CharBlock(max_length=100, required=True, help_text="Add your title")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("card_title", blocks.CharBlock(required=True, max_length=100)),
                ("card_subtitle", blocks.CharBlock(required=True, max_length = 200)),
            ]
        )
    )

    class Meta:
        template = "streams/board_members.html"
        icon = "placeholder"
        label = "Add Card"
