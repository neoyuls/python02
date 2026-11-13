#!/usr/bin/env python3

def garden_operations(operation_number):
    if operation_number == 0:
        print("Testing operation 0...")
        try:
            test = int('abc')
        except ValueError:
            print("Caught ValueError: ", end="")
            print(f"invalid literal for int() with base 10: {test}")
            return
    elif operation_number == 1:
        print("Testing operation 1...")
        try:
            return int(42 / 0)
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero")
            return
    elif operation_number == 2:
        try:
            filename = "/non/existent/file"
            return open(filename)
        except FileNotFoundError:
            print("Caught FileNotFoundError: [Errno 2] ")
            print(f"No such file or directory: '{filename}'")
    elif operation_number == 3:

