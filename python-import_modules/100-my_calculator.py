#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

operation_math = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

if __name__ == '__main__':
    lenArg = len(argv)
    operators = ['+', '-', '*', '/']

    if lenArg != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = argv[2]

    if not (operator in operators):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    op = operation_math[operator]

    print("{0} {1} {2} = {3}".format(a, operator, b, op(a, b)))
    exit(0)
