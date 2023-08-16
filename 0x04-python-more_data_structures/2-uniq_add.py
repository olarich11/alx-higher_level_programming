#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_list = []
    num = 0

    for i in my_list:
        if i not in uniq_list:
            uniq_list.append(i)
            num += i

    return num

if __name__ == "__main__":
    my_list = [1, 2, 2, 3, 4, 4, 5]
    result = uniq_add(my_list)
    print("Result:", result)
