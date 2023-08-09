#!/usr/bin/python3
import random

rand_num = random.randint(-10000, 10000)

if rand_num >= 0:
    last_digit = rand_num % 10
else:
    last_digit = ((rand_num * -1) % 10) * -1

result_message = "Last digit of %d is %d and is" % (rand_num, last_digit)

if last_digit == 0:
    print(result_message, "0")
elif last_digit > 5:
    print(result_message, "greater than 5")
else:
    print(result_message, "less than 6 and not 0")
