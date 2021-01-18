from django.contrib import admin
from django.urls import path

from house import views
from house.api import ApplyViewSet

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('proc', views.proc_view, name='proc_view'),
    path('admin', admin.site.urls),

    path('api/v1/apply/all', ApplyViewSet.as_view({'get': 'list'})),
]
