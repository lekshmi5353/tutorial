def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

number = int(input("Enter a number: "))
print(f"Factorial of {number}: {factorial(number)}")
