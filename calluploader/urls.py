from django.urls import path

from calluploader.views.show_form import show_form
from crmfields.views.reload import reload_start

urlpatterns = [
    path('upload-call/', show_form),
    path('', reload_start, name='reload_start')
]
