from django.db import models
from django.utils.translation import ugettext_lazy as _

from content_editor.models import Region, create_plugin_base

from feincms3 import plugins
from feincms3_meta.models import MetaMixin
from feincms3.mixins import RedirectMixin
from feincms3.pages import AbstractPage


class Page( RedirectMixin, MetaMixin, AbstractPage):
    regions = [
        Region( key="main", title=_("Main")),
    ]
    
    class Meta:
        ordering = ("position",)
        verbose_name = _("page")
        verbose_name_plural = _("pages")

PagePlugin = create_plugin_base( Page)


class RichText( plugins.richtext.RichText, PagePlugin):
    pass


class Image( plugins.image.Image, PagePlugin):
    caption = models.CharField( _("caption"), max_length=200, blank=True)
    css_class = models.CharField( _("CSS class"), max_length=5, default="left", 
        choices=( ("left",  _('Left')),
                  ("right", _('Right'))))
