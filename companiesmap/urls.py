from django.urls import path

from companiesmap.views.showmap import show_map
from crmfields.views.reload import reload_start

urlpatterns = [
    path('show_map/', show_map, name='show_map'),
    path('', reload_start, name='reload_start'),
]
