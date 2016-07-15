from django.conf.urls import patterns, url, include


urlpatterns = patterns(
    'bio.scheduler',
    url(r'action/(?P<action_id>\d*)/$', 'views.action', name="action"),
    url(r'actions/$', 'views.actions', name="actions"),
    url(r'^calendar/', include('schedule.urls'))
)
