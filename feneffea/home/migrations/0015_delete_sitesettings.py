# Generated by Django 4.1.7 on 2023-03-15 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_sitesettings'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SiteSettings',
        ),
    ]