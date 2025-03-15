number = int(input("Enter a number: "))
print(f"Prime factors of {number} are:")
factor = 2
while number > 1:
    while number % factor == 0:
        print(factor, end=" ")
        number //= factor
    factor += 1
