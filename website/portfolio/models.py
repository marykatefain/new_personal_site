from django.db import models

from wagtail.core import blocks

from wagtail.core.models import Page

from wagtail.core.fields import StreamField

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel

from website.blocks import ImageInfoSection


class PortfolioPage(Page):
    body = StreamField(
        [
            ('image_info_section', ImageInfoSection())
        ]
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
