# Generated by Django 4.1.7 on 2023-03-06 18:21

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_about_logo_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='content',
            field=wagtail.fields.StreamField([('board_members', wagtail.blocks.StructBlock([('p_name', wagtail.blocks.CharBlock(help_text='Enter Person Name', required=True)), ('p_position', wagtail.blocks.CharBlock(help_text='Enter Person Position', required=True)), ('p_desc', wagtail.blocks.TextBlock(help_text='Enter Person Description', required=False))]))], blank=True, null=True, use_json_field=None),
        ),
    ]
