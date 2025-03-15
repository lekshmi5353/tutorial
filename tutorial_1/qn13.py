number = int(input("Enter a number: "))
reversed_number = int(str(abs(number))[::-1]) * (-1 if number < 0 else 1)
print("Reversed number:", reversed_number)
