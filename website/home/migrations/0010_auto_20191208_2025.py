# Generated by Django 2.0.13 on 2019-12-08 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20191208_2024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='pagetitle',
            new_name='displaytitle',
        ),
    ]