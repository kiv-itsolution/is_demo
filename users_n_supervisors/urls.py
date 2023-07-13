from django.urls import path

from crmfields.views.reload import reload_start
from users_n_supervisors.views.actuallist import show_list

urlpatterns = [
    path('show_list/', show_list),
    path('', reload_start, name='reload_start'),
]
