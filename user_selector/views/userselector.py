from django.shortcuts import render
from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth


@main_auth(on_cookies=True)
def show_user(request):
    but = request.bitrix_user_token
    if request.method == 'POST':
        user_id = request.POST['selected_user']
        req_user = but.call_api_method('user.get', {'Id': user_id})['result'][0]
        field_list = ['ID', 'NAME', 'LAST_NAME', 'SECOND_NAME', 'EMAIL', 'PERSONAL_PHOTO']
        user_dict = dict()
        for key in field_list:
            try:
                user_dict.update({key: req_user[key]})
            except KeyError:
                pass

        return render(request, 'userselector.html', context={'req_user': user_dict})

    return render(request, 'userselector.html')
