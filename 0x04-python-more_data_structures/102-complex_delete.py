#!usr/bin/python3
def complex_delete(my_dictionary, value):
    keys_to_remove = []
    for key, val in my_dictionary.items():
        if val == value:
            keys_to_remove.append(key)

    for key in keys_to_remove:
        my_dictionary.pop(key)

    return my_dictionary
