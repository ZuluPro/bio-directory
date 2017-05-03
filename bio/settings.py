from django.conf import settings

USER_CAN_ADD_PLANT_FUNC = getattr(settings, 'BIO_USER_CAN_ADD_PLANT_FUNC', 'contribute.permissions.staff_only')
USER_CAN_VALIDATE_FUNC = getattr(settings, 'BIO_USER_CAN_VALIDATE_FUNC', 'contribute.permissions.staff_only')
USER_CAN_VOTE_FUNC = getattr(settings, 'BIO_USER_CAN_VOTE_FUNC', 'contribute.permissions.authenticated_only')
