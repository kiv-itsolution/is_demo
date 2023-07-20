from calluploader.views.show_form import show_form
from crmfields.views.reload import reload_start
from django.urls import path


urlpatterns = [
    path('upload-call/', show_form),
    path('', reload_start, name='reload_start')
]
