#!/usr/bin/python3

def print_error_message(exception):
    try:
        if isinstance(exception, TypeError):
            print("wrong type")
        elif isinstance(exception, ZeroDivisionError):
            print("division by 0")
        elif isinstance(exception, IndexError):
            print("out of range")
    except:
        pass

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except (TypeError, ZeroDivisionError, IndexError) as e:
            div = 0
            print_error_message(e)
        finally:
            new_list.append(div)
    return new_list
