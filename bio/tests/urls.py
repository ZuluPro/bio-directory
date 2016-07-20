from django.conf.urls import include, patterns, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from bio.urls import urlpatterns as bio_urls
from bio.guide.urls import urlpatterns as bio_guide_urls
from bio.items.urls import urlpatterns as bio_items_urls
from bio.scheduler.urls import urlpatterns as bio_scheduler_urls

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bio/', include(bio_urls)),
    url(r'^bio/', include(bio_guide_urls)),
    url(r'^bio/', include(bio_items_urls)),
    url(r'^bio/', include(bio_scheduler_urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
