import math

x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms: "))
sin_x = 0

for i in range(n):
    term = ((-1)**i / math.factorial(2*i + 1)) * (x**(2*i + 1))
    sin_x += term

print(f"sin({x}) up to {n} terms: {sin_x}")
