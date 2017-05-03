from bio import settings
from django.utils.module_loading import import_string


def staff_only(user):
    return user.is_superuser or user.is_staff


def authenticated_only(user):
    return bool(user.id)


def user_can_add_plant(user):
    func = import_string(settings.USER_CAN_ADD_PLANT_FUNC)
    return func(user)


def user_can_validate(user):
    func = import_string(settings.USER_CAN_VALIDATE_FUNC)
    return func(user)


def user_can_vote(user):
    func = import_string(settings.USER_CAN_VOTE_FUNC)
    return func(user)
