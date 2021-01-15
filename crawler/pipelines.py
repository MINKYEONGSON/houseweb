from house.models import Apply, ApplyHomeType


class CrawlerPipeline:
    def process_item(self, item, spider):
        def _check_apply(name):
            try:
                ins = Apply.objects.get(name=name)
                return ins
            except:
                return None

        if getattr(item, 'django_model') is Apply:
            item.save()
            return item

        if getattr(item, 'django_model') is ApplyHomeType:
            apply_name = item['apply']
            apply = _check_apply(apply_name)
            if apply is not None:
                item['apply'] = apply
                item.save()
                return item
