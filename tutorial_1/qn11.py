def sum_of_even_cubes(n):
    return sum(i**3 for i in range(2, n+1, 2))
try:
    n = int(input("Enter a positive integer n: "))
    if n <= 0:
        print("Please enter a positive integer greater than zero.")
    else:
        result = sum_of_even_cubes(n)
        print(f"The sum of cubes of all positive even numbers less than or equal to {n} is: {result}")
except ValueError:
    print("Invalid input. Please enter a positive integer.")
