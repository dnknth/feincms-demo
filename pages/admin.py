from django.contrib import admin
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _

from content_editor.admin import ContentEditor
from feincms3 import plugins
from feincms3.admin import TreeAdmin
from feincms3_meta.models import MetaMixin

from reversion.admin import VersionAdmin

from . import models


@admin.register( models.Page)
class PageAdmin( ContentEditor, TreeAdmin, VersionAdmin):
    list_display = ["indented_title", "move_column", "is_active"]
    list_filter = ['is_active']
    # list_editable = ['is_active']
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ["parent"]

    inlines = [
        plugins.richtext.RichTextInline.create( models.RichText),
        plugins.image.ImageInline.create( models.Image),
    ]

    fieldsets = [
        (None, {
            'fields': (
                'is_active',
                'parent',
                'title',
            )
        }),
        
        (capfirst(_('path')), {
            'fields': (
                'slug',
                'static_path',
                'path',
            ),
            'classes': ('tabbed', 'uncollapse'),
        }),
        
        MetaMixin.admin_fieldset(),

        (capfirst(_('redirect')), {
            'fields': (
                'redirect_to_page',
                'redirect_to_url',
            ),
            'classes': ('tabbed',),
        }),
    ]

    class Media:
        js = ( 'admin/js/jquery.init.js', 'pages/plugin_buttons.js', )
        css =  { 'all' : ('https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css', ) }
