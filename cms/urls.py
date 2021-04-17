from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path


app_name = "pages"

urlpatterns = [
    path( 'accounts/', include('django.contrib.auth.urls')),
    path( 'admin/doc/', include('django.contrib.admindocs.urls')),
    path( 'admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path( '__debug__/', include( debug_toolbar.urls)),
    ]
    urlpatterns += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
urlpatterns += [
    path( '', include( 'pages.urls')),
]
