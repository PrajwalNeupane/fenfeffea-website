# Generated by Django 4.1.7 on 2023-03-06 19:03

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_alter_about_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='content',
            field=wagtail.fields.StreamField([('board_members', wagtail.blocks.StructBlock([('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('full_name', wagtail.blocks.CharBlock(max_length=100, required=True)), ('position', wagtail.blocks.CharBlock(max_length=200, required=True)), ('button_page', wagtail.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.blocks.URLBlock(required=False))])))]))], blank=True, null=True, use_json_field=None),
        ),
    ]
