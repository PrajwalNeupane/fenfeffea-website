# Generated by Django 4.1.7 on 2023-03-16 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_homepage_panel_img1_homepage_panel_img2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='link1_url',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='link2_url',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='link3_url',
            field=models.CharField(max_length=100, null=True),
        ),
    ]