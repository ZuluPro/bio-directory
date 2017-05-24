from bio import settings
from bio.utils import import_model_class


class Tag(import_model_class(settings.BASE_TAG_MODEL)):
    class Meta:
        proxy = True
