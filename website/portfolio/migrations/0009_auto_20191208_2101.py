# Generated by Django 2.0.13 on 2019-12-08 21:01

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20191208_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliopage',
            name='body',
            field=wagtail.core.fields.StreamField([('image_info_section', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock()), ('slug', wagtail.core.blocks.CharBlock(required=False)), ('body', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))]))]),
        ),
    ]
