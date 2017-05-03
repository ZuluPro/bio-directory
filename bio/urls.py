from django.conf.urls import patterns, url
from . import views
from contribute import views as contribute_views


urlpatterns = patterns(
    'bio',
    url(r'^$', views.HomeView.as_view(), name='home'),

    url(r'plants/$', views.PlantListView.as_view(), name="plants"),
    url(r'plants/(?P<plant_id>\d*)/$', 'views.plant', name="plant"),

    url(r'contribute/$', contribute_views.HomeView.as_view(), name='contribute-home'),
    url(r'contribute/plant/$', contribute_views.ChoosePlantQuestionView.as_view(), name='contribute-plant'),
    url(r'contribute/plant/(?P<pk>\d+)/$', contribute_views.PlantView.as_view(), name='contribute-plant-home'),
    url(r'contribute/plant/(?P<pk>\d+)/question/$', contribute_views.PlantQuestionView.as_view(), name='contribute-plant-question'),
    url(r'contribute/plant/(?P<pk>\d+)/add_image/$', contribute_views.AddPlantImageFormView.as_view(), name='contribute-plant-add-image'),

    # Validation
    url(r'contribute/validate/$', contribute_views.ValidationHomeView.as_view(), name='contribute-validation-home'),

    url(r'contribute/validate/new_plant/$', contribute_views.ValidateNewPlantQuestionListView.as_view(), name='contribute-new-plant-question-validate-list'),
    url(r'contribute/validate/new_plant/auto$', contribute_views.ValidateNewPlantQuestionAutoPickView.as_view(), name='contribute-new-plant-question-validate-auto-pick'),
    url(r'contribute/validate/new_plant/(?P<pk>\d+)/$', contribute_views.ValidateNewPlantView.as_view(), name='contribute-new-plant-question-validate'),

    url(r'contribute/validate/plant_image/auto/$', contribute_views.ValidateNewPlantImageAutoPickView.as_view(), name='contribute-plant-image-validate-auto-pick'),
    url(r'contribute/validate/plant_image/$', contribute_views.ValidatePlantImageListView.as_view(), name='contribute-plant-image-validate-list'),
    url(r'contribute/validate/plant_image/(?P<pk>\d+)/$', contribute_views.ValidatePlantImageView.as_view(), name='contribute-plant-image-validate'),

    url(r'contribute/validate/plant/$', contribute_views.ValidatePlantQuestionListView.as_view(), name='contribute-plant-question-validate-list'),
    url(r'contribute/validate/plant/auto$', contribute_views.ValidatePlantQuestionAutoPickView.as_view(), name='contribute-plant-question-validate-auto-pick'),
    url(r'contribute/validate/plant/(?P<pk>\d+)/$', contribute_views.ValidatePlantQuestionView.as_view(), name='contribute-plant-question-validate'),

    url(r'directories/$', 'views.directories', name="directories"),
    url(r'pathology/(?P<pathology_id>\d*)/$', 'views.pathology', name="pathology"),
    url(r'pathologies/$', 'views.pathologies', name="pathologies"),
)
