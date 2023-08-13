#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    fresh_list = []
    for value in my_list:
        fresh_list.append(value % 2 == 0)
    return fresh_list
