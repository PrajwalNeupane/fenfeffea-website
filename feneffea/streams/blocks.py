from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class Cards(blocks.StructBlock):
    card_group_title = blocks.CharBlock(
        max_length=100, required=True, help_text="Add your title"
    )

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("card_title", blocks.CharBlock(required=True, max_length=100)),
                ("card_subtitle", blocks.CharBlock(required=True, max_length=200)),
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


class ImgGallery(blocks.StructBlock):
    first_img = ImageChooserBlock(required=True)
    first_img_desc = blocks.CharBlock(required=True, max_length=100)

    images = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("img", ImageChooserBlock(required=True)),
                ("img_desc", blocks.CharBlock(required=True, max_length=100)),
            ]
        )
    )

    class Meta:
        template = "streams/ImgGallery.html"
        icon = "placeholder"
        label = "Add Image to Gallery"


class BoardHistoryAccordion(blocks.StructBlock):
    first_header = blocks.CharBlock(required=True, max_length=100)
    first_img = ImageChooserBlock(required=True)

    board_history_accordion = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("board_list_img", ImageChooserBlock(required=True)),
                (
                    "board_history_header",
                    blocks.CharBlock(required=True, max_length=100),
                ),
            ]
        )
    )

    class Meta:
        template = "streams/Board_History_Accordion.html"
        icon = "placeholder"
        label = "Add Board History"


class MainCarousel(blocks.StructBlock):
    first_img = ImageChooserBlock(required=True)
    first_img_desc = blocks.CharBlock(required=True, max_length=100)

    images = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("img", ImageChooserBlock(required=True)),
                ("img_desc", blocks.CharBlock(required=True, max_length=100)),
            ]
        )
    )

    class Meta:
        template = "streams/ImgGallery.html"
        icon = "image"
        label = "Add Image to Carousel"
