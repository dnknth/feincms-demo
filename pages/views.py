from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

from feincms3_meta.utils import meta_tags
from feincms3.regions import Regions

from haystack.views import SearchView as HaystackSearchView

from .models import *
from .renderers import html_renderer, json_renderer


class JSONRegions( Regions):

    def render(self, region, context=None):
        return [
            dict(
                self.renderer.render_plugin_in_context(plugin),
                type=plugin.__class__.__name__,
            )
            for plugin in self.contents[region]
        ]


def root( request):
    "Redirect to first page"
    
    page = Page.objects.active().first()
    if page is None:
        raise Http404( 'No page available')
    return redirect( page.get_absolute_url())

        
def page_detail( request, path):
    "Send a apge either as HTML or JSON"

    # Handle redirects
    page = get_object_or_404( Page, path="/%s/" % path, is_active=True)
    if page.redirect_to_url or page.redirect_to_page:
        return redirect( page.redirect_to_url or page.redirect_to_page)

    # Handle JSON
    if request.is_ajax():
        return JsonResponse({
            "id": page.pk,
            "title": page.title,
            "content": JSONRegions.from_item(
                page, renderer=json_renderer).render( "main"),
        })

    # Prepare context vars
    ancestors = list( page.ancestors().reverse())
    links = page.children.active() or (
        page.parent.children.active() if page.parent_id else [])
        
    # Render HTML
    return render( request, "pages/page.html", {
        "page": page,
        "regions": Regions.from_item( page,
            renderer=html_renderer, inherit_from=ancestors),
        "links" : links,
        "meta_tags": meta_tags( [page] + ancestors, request=request),
    })


class SearchView( HaystackSearchView):
    "Search view with AJAX support"
    
    def __init__( self, **kwargs):
        super().__init__( **kwargs)

    def __call__( self, request):
        response = super().__call__( request)

        if request.is_ajax():
            return JsonResponse([{
                    "uri" : r.object.get_absolute_url(), 
                    "title" : r.object.title
                } for r in self.results.load_all() 
            ], safe=False)
        
        return response
