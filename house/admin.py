from django.contrib import admin
from django.utils.safestring import mark_safe

from house.models import Apply


@admin.register(Apply)
class ApplyAdmin(admin.ModelAdmin):
    list_display = ['id', 'site', 'name', 'type1', 'type2', 'home_count_str',
                    'vote_date__str', 'apply_home_type_set_10_str', 'apply_home_type_set_20_str',
                    'apply_home_type_set_30_str', 'apply_home_type_set_big_str']
    list_filter = ['site', 'type1', 'type2']

    # @staticmethod
    # def name_str(self):
    #     data = self.name
    #
    #     return self.name +

    @staticmethod
    def home_count_str(self):
        return self.home_count + '세대'

    @staticmethod
    def vote_date__str(self):
        data = ''
        if self.vote_tk is not None:
            data += '[특공] %s<br/>' % (self.vote_tk)
        if self.vote_1 is not None:
            data += '[1순위] %s<br/>' % (self.vote_1)
        if self.vote_2 is not None:
            data += '[2순위] %s<br/>' % (self.vote_2)
        return mark_safe('<pre>' + data + '</pre>')

    @staticmethod
    def apply_home_type_set_10_str(self):
        data = ''
        for home in list(self.applyhometype_set.all()):
            if home.price is not None:
                tmp = str(round(home.price / 10000, 1)) + '억'
                name = ''
                tmp1 = home.name.replace(' ', '')
                for index in range(len(tmp1), 1, -1):
                    try:
                        name = float(tmp1[:index])
                        break
                    except:
                        pass
                if int(name * 0.3025) >= 10 and int(name * 0.3025) < 20:
                    data += '[%s평/%s형] %s<br/>' % (int(name * 0.3025), home.name, tmp)
        return mark_safe('<pre>' + data + '</pre>')

    apply_home_type_set_10_str.verbose_name = '10평대'

    @staticmethod
    def apply_home_type_set_20_str(self):
        data = ''
        for home in list(self.applyhometype_set.all()):
            if home.price is not None:
                tmp = str(round(home.price / 10000, 1)) + '억'
                name = ''
                tmp1 = home.name.replace(' ', '')
                for index in range(len(tmp1), 1, -1):
                    try:
                        name = float(tmp1[:index])
                        break
                    except:
                        pass
                if int(name * 0.3025) >= 20 and int(name * 0.3025) < 30:
                    data += '[%s평/%s형] %s<br/>' % (int(name * 0.3025), home.name, tmp)
        return mark_safe('<pre>' + data + '</pre>')

    @staticmethod
    def apply_home_type_set_30_str(self):
        data = ''
        for home in list(self.applyhometype_set.all()):
            if home.price is not None:
                tmp = str(round(home.price / 10000, 1)) + '억'
                name = ''
                tmp1 = home.name.replace(' ', '')
                for index in range(len(tmp1), 1, -1):
                    try:
                        name = float(tmp1[:index])
                        break
                    except:
                        pass
                if int(name * 0.3025) >= 30 and int(name * 0.3025) < 40:
                    data += '[%s평/%s형] %s<br/>' % (int(name * 0.3025), home.name, tmp)
        return mark_safe('<pre>' + data + '</pre>')

    @staticmethod
    def apply_home_type_set_big_str(self):
        data = ''
        for home in list(self.applyhometype_set.all()):
            if home.price is not None:
                tmp = str(round(home.price / 10000, 1)) + '억'
                name = ''
                tmp1 = home.name.replace(' ', '')
                for index in range(len(tmp1), 1, -1):
                    try:
                        name = float(tmp1[:index])
                        break
                    except:
                        pass
                if int(name * 0.3025) >= 40:
                    data += '[%s평/%s형] %s<br/>' % (int(name * 0.3025), home.name, tmp)
        return mark_safe('<pre>' + data + '</pre>')
