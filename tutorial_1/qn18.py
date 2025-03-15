number = int(input("Enter a number: "))
num_str = str(number)
n = len(num_str)
armstrong_sum = sum(int(digit)**n for digit in num_str)
if number == armstrong_sum:
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")
