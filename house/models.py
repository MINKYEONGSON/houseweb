from django.db import models


class Apply(models.Model):
    name = models.CharField(max_length=150, verbose_name='주택명')

    site = models.CharField(max_length=150, verbose_name='도시')
    type1 = models.CharField(max_length=150, verbose_name='주택구분')
    type2 = models.CharField(max_length=150, verbose_name='분양/임대')

    publish_date = models.DateField(max_length=150, verbose_name='모집공고일')
    start_date = models.DateField(max_length=150)
    end_date = models.DateField(max_length=150)

    address = models.CharField(max_length=150, verbose_name='주소')
    home_count = models.CharField(max_length=150, verbose_name='세대수')

    vote_tk = models.DateField(null=True, verbose_name='특공(해당)')
    vote_1 = models.DateField(null=True, verbose_name='1순위(해당)')
    vote_2 = models.DateField(null=True, verbose_name='2순위(해당)')
    vote_n = models.DateField(null=True, verbose_name='무순위')
    url = models.URLField(null=True, blank=True)


class ApplyHomeType(models.Model):
    apply = models.ForeignKey(Apply, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    price = models.IntegerField(null=True)
