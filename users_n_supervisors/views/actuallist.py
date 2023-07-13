from django.shortcuts import render
from pprint import pprint
from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth
from users_n_supervisors.utils import find_head


@main_auth(on_cookies=True)
def show_list(request):
    but = request.bitrix_user_token

    #  Юзера
    res = but.call_list_method('user.get')
    users = [[i['ID'], f"{i['NAME']} {i['LAST_NAME']}", i['UF_DEPARTMENT']] for i in res]
    user_dict = {}
    for i in users:
        user_dict[int(i[0])] = {'name': i[1], 'deps': i[2]}
    # pprint(user_dict)

    #  Департаменты
    departments = but.call_list_method('department.get')
    # print(departments)
    departments_dict = {}
    for dep in departments:
        if 'PARENT' not in dep:
            departments_dict[int(f"{dep['ID']}")] = {'name': dep['NAME'], 'uf_head': int(dep['UF_HEAD'])}
        elif 'PARENT' in dep and 'UF_HEAD' in dep:
            departments_dict[int(f"{dep['ID']}")] = {'name': dep['NAME'], 'parent': int(dep['PARENT']),
                                                     'uf_head': int(dep['UF_HEAD'])}
        else:
            departments_dict[int(f"{dep['ID']}")] = {'name': dep['NAME'], 'parent': int(dep['PARENT'])}

    # pprint(departments_dict)

    # Записываем результат
    result = dict()
    for employee_id in user_dict.keys():
        supervisor = find_head(employee_id, departments_dict, user_dict)
        result[employee_id] = supervisor
    # pprint(result)
    return render(request, 'showuserslist.html', context={'users_n_supers': result})
