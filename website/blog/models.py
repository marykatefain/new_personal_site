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


class BlogIndexPage(Page):
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

    subpage_types = ['BlogPostPage']

    def get_context(self, request):
        context = super(BlogIndexPage, self).get_context(request)
        context['blog_pages'] = self.get_children().type(BlogPostPage)
        return context


class BlogPostPage(Page):
    body = StreamField([
        ('content', blocks.RichTextBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    parent_page_types = ['BlogIndexPage']
