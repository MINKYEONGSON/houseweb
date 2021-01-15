from scrapy_djangoitem import DjangoItem

from house.models import Apply, ApplyHomeType


class ApplyItem(DjangoItem):
    django_model = Apply


class ApplyHomeTypeItem(DjangoItem):
    django_model = ApplyHomeType
