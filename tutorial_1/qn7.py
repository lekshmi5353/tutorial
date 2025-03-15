x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))
if x > 0 and y > 0:
    print("Point is in Quadrant I")
elif x < 0 and y > 0:
    print("Point is in Quadrant II")
elif x < 0 and y < 0:
    print("Point is in Quadrant III")
elif x > 0 and y < 0:
    print("Point is in Quadrant IV")
else:
    print("The point lies on an axis")
