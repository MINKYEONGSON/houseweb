from django.shortcuts import render, redirect
from scrapyd_api import ScrapydAPI

from house.models import Apply


def index_view(request):
    return render(request, template_name='index.html', context={})


def proc_view(request):
    Apply.objects.all().delete()
    scrapyd = ScrapydAPI('http://localhost:6800')
    scrapyd.schedule('default', 'applyhome')
    scrapyd.schedule('default', 'applyhome_moo')
    return redirect('/')
