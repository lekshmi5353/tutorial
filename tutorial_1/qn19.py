n = int(input("How many numbers? "))
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(n)]
even_count = sum(1 for num in numbers if num % 2 == 0)
odd_count = n - even_count
print(f"Even numbers: {even_count}, Odd numbers: {odd_count}")
