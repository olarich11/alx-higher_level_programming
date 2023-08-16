#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_elements = []
    total_sum = 0

    for num in my_list:
        if num not in unique_elements:
            unique_elements.append(num)
            total_sum += num

    return total_sum
