#!usr/bin/python3
def complex_delete(my_dict, value):
    keys_to_remove = []
    for key, val in my_dict.items():
        if val == value:
            keys_to_remove.append(key)

    for key in keys_to_remove:
        my_dict.pop(key)

    return my_dict
