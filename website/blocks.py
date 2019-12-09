from django.db import models

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class ImageInfoSection(blocks.StructBlock):
    headline = blocks.CharBlock(required=True)
    slug = blocks.CharBlock(required=True)
    body = blocks.RichTextBlock(required=False)
    image = ImageChooserBlock(required=False)

    class Meta:
        template = 'website/blocks/image_info_section.html'
        icon = 'fa-paragraph'

class HomeSection(blocks.StructBlock):
    headline = blocks.CharBlock(required=True)
    slug = blocks.CharBlock(required=True)
    body = blocks.RichTextBlock(required=False)
    image = ImageChooserBlock(required=False)

    class Meta:
        template = 'website/blocks/home_section.html'
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


class PortfolioCard(blocks.StructBlock):
    link = blocks.URLBlock()
    image = ImageChooserBlock()
    headline = blocks.CharBlock(required=True)
    subtitle = blocks.CharBlock(required=False)
    body = blocks.RichTextBlock(required=False)
    technologies = blocks.CharBlock(required=False)

    class Meta:
        template = 'website/blocks/portfolio_card.html'
        icon = 'fa-paragraph'
