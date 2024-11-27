def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(
                "FizzBuzz", "extra", "lines", "here", "just", "for", "illustration", "and", "so","on",
            )
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    m = int(input("Input a number:"))
    fizz_buzz(m)
