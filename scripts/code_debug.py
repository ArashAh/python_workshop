def divide_numbers(num1, num2):
    return num1 / num2


def greet_user(name):
    print("Hello, " + name.upper())


def multiply(a, b):
    return a * b


def add(a, b):
    return a + b


def calculate_area(length, width):
    print("Calculating area.")
    area = multiply(length, width)
    print(f"Area calculated: {area}")
    return area


def calculate_perimeter(length, width):
    print("Calculating perimeter.")
    perimeter = add(add(length, width), add(length, width))
    print(f"Perimeter calculated: {perimeter}")
    return perimeter


def run_calcs():
    length = 5
    width = 3
    print("Starting calculations.")
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)
    print(f"Area: {area}, Perimeter: {perimeter}")


nums = [10, 0, 5]
names = ["Alice", "Bob", None]

# Error 1: Attempt to divide by zero
result = divide_numbers(nums[0], nums[1])

# Error 2: Attempt to format a None value
greet_user(names[2])


# Test "Step into" and "Step out"
run_calcs()
