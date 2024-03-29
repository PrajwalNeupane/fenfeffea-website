# Generated by Django 4.1.7 on 2023-03-16 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('contactform', '0002_contactform_logo_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='contact_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
