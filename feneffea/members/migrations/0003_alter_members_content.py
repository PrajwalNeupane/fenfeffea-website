# Generated by Django 4.1.7 on 2023-03-15 16:37

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_members_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='content',
            field=wagtail.fields.StreamField([('board_members', wagtail.blocks.StructBlock([('card_group_title', wagtail.blocks.CharBlock(help_text='Add your title', max_length=100, required=True)), ('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('card_title', wagtail.blocks.CharBlock(max_length=100, required=True)), ('card_subtitle', wagtail.blocks.CharBlock(max_length=200, required=True))])))]))], blank=True, null=True, use_json_field=None),
        ),
    ]
