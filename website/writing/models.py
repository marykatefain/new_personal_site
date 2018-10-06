from django.db import models

from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    MultiFieldPanel,
    InlinePanel,
    PageChooserPanel,
    StreamFieldPanel
)


class WritingPage(Page):
    body = StreamField([
        ('content', blocks.RichTextBlock()),
    ], null=True, blank=True)

    sidebar = StreamField([
        ('content', blocks.RichTextBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
        StreamFieldPanel('sidebar'),

    ]
