# Generated by Django 2.0.9 on 2018-10-12 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogindexpage',
            name='body',
        ),
        migrations.RemoveField(
            model_name='blogindexpage',
            name='sidebar',
        ),
    ]
