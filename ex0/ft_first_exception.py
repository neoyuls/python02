#!/usr/bin/env python3

def input_temperature(temp_str):
    try:
        return int(temp_str)
    except ValueError:
        print("Caught input_temperature error: ", end="")
        print(f"invalid literal for int() with base 10: '{temp_str}'")


def test_temperature():
    print("=== Garden Temperature ===\n")
    print("Input data is: '25'")
    print(f"Temperature is now {input_temperature('25')}°C\n")
    print("Input data is: 'abc'")
    input_temperature('abc')
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
