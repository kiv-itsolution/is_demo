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
            # cur_call = CallModel.objects.filter(user_phone_inner=form.data['user_phone_inner'],
            #                                     phone_number=form.data['phone_number'],
            #                                     call_start_date=form.data['call_start_date'],
            #                                     type=form.data['type'],
            #                                     )
            instance.register_call_id(but)
            instance.finish(but)
            return render(request, 'form.html', context={'form': form})
    return render(request, 'form.html', context={'form': form})
