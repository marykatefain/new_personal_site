# Generated by Django 2.0.9 on 2018-10-12 20:56

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181012_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpostpage',
            name='body',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
    ]
