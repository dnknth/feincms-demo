from django.conf import settings
from django.utils.html import format_html, mark_safe

from feincms3.renderer import TemplatePluginRenderer

from .models import *


html_renderer = TemplatePluginRenderer()

html_renderer.register_string_renderer(
    RichText,
    lambda plugin: mark_safe( plugin.text),
)

html_renderer.register_string_renderer(
    Image,
    lambda plugin: format_html(
        '<img src="{}" alt="{}" class="{}"/>',
        plugin.image.url,
        plugin.caption,
        plugin.css_class,
    ),
)


json_renderer = TemplatePluginRenderer()

json_renderer.register_string_renderer(
    RichText,
    lambda plugin: { "text": plugin.text },
)

json_renderer.register_string_renderer(
    Image,
    lambda plugin: {
        "image": plugin.image.url,
        "caption": plugin.caption },
)

