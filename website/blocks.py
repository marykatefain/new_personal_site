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


class PortalCard(blocks.StructBlock):
    link = blocks.ListBlock(blocks.PageChooserBlock())
    image = ImageChooserBlock()
    headline = blocks.CharBlock(required=True)
    subtitle = blocks.CharBlock(required=False)
    body = blocks.RichTextBlock(required=False)

    class Meta:
        template = 'website/blocks/portal_card.html'
        icon = 'fa-paragraph'
