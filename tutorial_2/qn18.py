def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter the position (n): "))
print(f"The {n}'th Fibonacci number is: {fibonacci(n)}")
