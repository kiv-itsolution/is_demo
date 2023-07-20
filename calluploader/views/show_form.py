from django.shortcuts import render

from calluploader.forms.callform import CustomCallForm
from calluploader.models import CallModel
from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth


@main_auth(on_cookies=True)
def show_form(request):
    form = CustomCallForm()
    if request.method == "POST":
        form = CustomCallForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            but = request.bitrix_user_token

            instance.register_call_id(but)
            instance.finish(but)
            return render(request, 'form.html', context={'form': form})
    return render(request, 'form.html', context={'form': form})
