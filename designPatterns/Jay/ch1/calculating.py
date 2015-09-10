
import sys

def divide(a, b):
    if b == 0:
        return 0
    return a / b

def multiply(a, b):
    return a * b

def sub(a, b):
    return a - b

def add(a, b):
    return a + b

def main():
    opMap = {
        "+" : add,
        "-" : sub,
        "*" : multiply,
        "/" : divide,
    }
    a = raw_input("Enter first number:")
    b = raw_input("Enter second number:")
    op = raw_input("Enter operation:(+,-,*,/)")

    print "result:", opMap[op](int(a), int(b))



if __name__ == "__main__":
    main()
