from importlib import import_module
from django.core.exceptions import ImproperlyConfigured
from django.core.files.storage import get_storage_class
from bio import settings


def import_model_class(model_path):
    dot = model_path.rindex('.')
    module_name = model_path[:dot]
    class_name = model_path[dot + 1:]
    try:
        _class = getattr(import_module(module_name), class_name)
        return _class
    except IOError:
        raise ImproperlyConfigured('%s cannot be imported' % model_path)


def get_media_storage(path=None, options=None):
    path = path or settings.MEDIA_STORAGE
    options = options or settings.MEDIA_STORAGE_OPTIONS
    storage_class = get_storage_class(path)
    storage = storage_class(**options)
    return storage
