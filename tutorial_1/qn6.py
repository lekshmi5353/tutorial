a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))
sides = sorted([a, b, c])
if sides[0]**2 + sides[1]**2 == sides[2]**2:
    print("It is a right-angled triangle")
else:
    print("It is not a right-angled triangle")
