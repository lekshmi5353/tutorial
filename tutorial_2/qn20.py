n = int(input("How many numbers? "))
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(n)]
even_sum = sum(num for num in numbers if num % 2 == 0)
print("Sum of even numbers:", even_sum)
