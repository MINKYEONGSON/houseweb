import json

from django.shortcuts import render


# Create your views here.
def index_view(request):
    f = open('C:\\Users\\itf-infra\\Documents\\GitHub\\house\\house\\items.json', 'r', encoding='utf-8')
    data = f.read()
    jaon_data = json.loads(data)
    return render(request, template_name='index.html', context={'json_data': jaon_data})
