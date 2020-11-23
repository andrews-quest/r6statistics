def sort(operators_list):
    operators_list.sort(key=lambda x: x[1])
    return operators_list