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

class Pubs(blocks.StructBlock):


    books = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("pubs_image", ImageChooserBlock(required=True)),
                ("pubs_title", blocks.CharBlock(required=True, max_length=100)),
                ("pubs_detail", blocks.TextBlock(required=True)),
            ]
        )
    )

    class Meta:
        template = "streams/pubs.html"
        icon = "placeholder"
        label = "Add Publication"