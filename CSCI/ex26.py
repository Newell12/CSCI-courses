def get_highest_paid(employees):
    max = 0
    maxname = ''
    for name in employees:
        if employees.get(name).get('Salary')>max:
            max = employees.get(name).get('Salary')
            maxname = name
    return maxname
