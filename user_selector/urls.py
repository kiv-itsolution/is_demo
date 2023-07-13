from django.urls import path
from crmfields.views.reload import reload_start
from user_selector.views.userselector import show_user

urlpatterns = [
    path('show_user/', show_user, name='show_user'),
    path('', reload_start, name='reload_start'),
]
