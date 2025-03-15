names = input("Enter names separated by commas: ").split(',')
names = [name.strip() for name in names]
names.sort()
print("Sorted names:", names)
