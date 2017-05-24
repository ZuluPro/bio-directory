from django.conf import settings

USER_CAN_ADD_PLANT_FUNC = getattr(settings, 'BIO_USER_CAN_ADD_PLANT_FUNC', 'contribute.permissions.staff_only')
USER_CAN_VALIDATE_FUNC = getattr(settings, 'BIO_USER_CAN_VALIDATE_FUNC', 'contribute.permissions.staff_only')
USER_CAN_VOTE_FUNC = getattr(settings, 'BIO_USER_CAN_VOTE_FUNC', 'contribute.permissions.authenticated_only')

BASE_TAG_MODEL = getattr(settings, 'BIO_BASE_TAG_MODEL', 'bio.models_base.Tag')

MEDIA_STORAGE = getattr(settings, 'BIO_MEDIA_STORAGE', settings.DEFAULT_FILE_STORAGE)
MEDIA_STORAGE_OPTIONS = getattr(settings, 'BIO_MEDIA_STORAGE_OPTIONS', {})
