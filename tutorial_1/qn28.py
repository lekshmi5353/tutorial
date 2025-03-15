lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))
sum_of_odds = sum(num for num in range(lower, upper+1) if num % 2 != 0)
print(f"Sum of odd numbers between {lower} and {upper}: {sum_of_odds}")
