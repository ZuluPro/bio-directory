from django.conf.urls import include, patterns, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from bio.urls import urlpatterns as bio_urls
from bio.items.urls import urlpatterns as bio_items_urls

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bio/', include(bio_urls)),
    url(r'^bio/', include(bio_items_urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
