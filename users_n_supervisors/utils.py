def find_head(employee_id, departments, employees):
    employee = employees[employee_id]
    department_ids = employee['deps']
    supervisors = []

    for department_id in department_ids:
        if department_id in departments:
            department = departments[department_id]
            supervisor_id = None

            # Ищем начальника по полю 'uf_head'
            if 'uf_head' in department and department['uf_head'] != 0:
                supervisor_id = department['uf_head']

            # Если начальник не найден, ищем начальника по полю 'parent' с использованием цикла
            if supervisor_id is None and 'parent' in department:
                parent_id = department['parent']
                while parent_id is not None and supervisor_id is None:
                    parent_department = departments[parent_id]
                    if 'uf_head' in parent_department and parent_department['uf_head'] != 0:
                        supervisor_id = parent_department['uf_head']
                    parent_id = parent_department.get('parent')

            # Если начальник найден и отличается от сотрудника, добавляем его в список начальников
            if supervisor_id and supervisor_id != employee_id and supervisor_id in employees and 'name' in employees[
                supervisor_id]:
                supervisor_name = employees[supervisor_id]['name']
                supervisors.append(supervisor_name)

    return {'name': employee['name'], 'supervisors': supervisors}
