def sum_of_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)
try:
    n = int(input("Enter the number of elements: "))
    if n <= 0:
        print("The number of elements must be positive.")
    else:
        numbers = []
        for i in range(n):
            num = int(input(f"Enter number {i+1}: "))
            numbers.append(num)
        result = sum_of_even_numbers(numbers)
        print(f"The sum of even numbers is: {result}")
except ValueError:
    print("Invalid input. Please enter integers.")
