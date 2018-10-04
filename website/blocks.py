from django.db import models

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class ImageInfoSection(blocks.StructBlock):
    headline = blocks.CharBlock(required=False)
    body = blocks.RichTextBlock(required=False)
    image = ImageChooserBlock()

    class Meta:
        template = 'website/blocks/image_info_section.html'
        icon = 'fa-paragraph'
