from django.conf.urls import patterns, url


urlpatterns = patterns(
    'bio.items',
    url(r'plantitem/(?P<plant_id>\d*)/$', 'views.plantitem', name="plantitem"),
    url(r'plantitems/$', 'views.plantitems', name="plantitems"),
)
