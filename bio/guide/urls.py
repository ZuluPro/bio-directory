from django.conf.urls import patterns, url


urlpatterns = patterns(
    'bio.guide',
    url(r'guide/(?P<guide_id>\d*)/$', 'views.guide', name="guide"),
    url(r'guides/$', 'views.guides', name="guides"),
)
