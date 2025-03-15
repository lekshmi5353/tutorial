number = int(input("Enter a number: "))
sum_of_digits = sum(int(digit) for digit in str(abs(number)))
print("Sum of digits:", sum_of_digits)
