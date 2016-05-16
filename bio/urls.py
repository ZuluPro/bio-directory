from django.conf.urls import patterns, url


urlpatterns = patterns(
    'bio',
    url(r'directories/$', 'views.directories', name="directories"),
    url(r'plant/(?P<plant_id>\d*)/$', 'views.plant', name="plant"),
    url(r'plants/$', 'views.plants', name="plants"),
    url(r'pathology/(?P<pathology_id>\d*)/$', 'views.pathology', name="pathology"),
    url(r'pathologies/$', 'views.pathologies', name="pathologies"),
    url(r'pest/(?P<pest_id>\d*)/$', 'views.pest', name="pest"),
    url(r'pests/$', 'views.pests', name="pests"),
)
