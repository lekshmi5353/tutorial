x = int(input("Enter the base (X): "))
y = int(input("Enter the exponent (Y): "))
result = 1
for _ in range(abs(y)):
    result *= x
if y < 0:
    result = 1 / result
print(f"{x}^{y} = {result}")
