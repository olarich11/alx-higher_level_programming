#!/usr/bin/python3

for num in range(0, 99):
    if num != 98:
        print("{:d} = 0x{:x}".format(num, num))
    else:
        print("{:d} = 0x{:x}".format(num, num), end='\n')
