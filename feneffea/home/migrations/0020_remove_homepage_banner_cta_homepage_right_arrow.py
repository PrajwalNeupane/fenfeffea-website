# Generated by Django 4.1.7 on 2023-03-17 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('home', '0019_homepage_pub_panel_img1_homepage_pub_panel_img2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='banner_cta',
        ),
        migrations.AddField(
            model_name='homepage',
            name='right_arrow',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
