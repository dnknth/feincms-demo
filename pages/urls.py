from django.urls import path, re_path
from django.views.static import serve

from . import views

app_name = "pages"

urlpatterns = [
    path( '', views.root, name="root"),
    path( 'search/', views.SearchView(), name='haystack_search'),
    re_path( r"^(?P<path>[-\w/]+)/$", views.page_detail, name="page"),
]
