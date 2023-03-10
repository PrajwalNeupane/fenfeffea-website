# Generated by Django 4.1.7 on 2023-03-08 16:12

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_banner_subtitle_homepage_home_message_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='events',
            field=wagtail.fields.StreamField([('event_listings', wagtail.blocks.StructBlock([('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('card_title', wagtail.blocks.CharBlock(max_length=100, required=True)), ('card_subtitle', wagtail.blocks.CharBlock(max_length=200, required=True)), ('button_page', wagtail.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.blocks.URLBlock(required=False))])))]))], blank=True, null=True, use_json_field=None),
        ),
    ]