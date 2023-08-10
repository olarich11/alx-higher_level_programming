#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    if len(argv) != 4:
        print('Usage: {} <a> <operator> <b>'.format(argv[0]))
        exit(1)

    num1 = int(argv[1])
    operator = argv[2]
    num2 = int(argv[3])

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 // num2
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    print('{:d} {:s} {:d} = {:d}'.format(num1, operator, num2, result))
