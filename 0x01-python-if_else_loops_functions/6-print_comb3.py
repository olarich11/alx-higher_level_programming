#!/usr/bin/python3

for num1 in range(0, 9):
    for num2 in range(num1 + 1, 10):
        sep = ', ' if (num1 != 8 or num2 != 9) else '\n'
        print("{:02d}".format(num1 * 10 + num2), end=sep)
