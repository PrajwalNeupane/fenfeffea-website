# Generated by Django 4.1.7 on 2023-03-14 13:12

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0011_about_home_message_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='about_feneffea',
            field=wagtail.fields.RichTextField(null=True),
        ),
    ]
