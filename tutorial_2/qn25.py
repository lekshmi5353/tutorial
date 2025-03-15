data = input("Enter a list of mixed data types (e.g., 1, 2.3, 'hello'): ").split(', ')
integers = [int(x) for x in data if x.isdigit()]
floats = [float(x) for x in data if x.replace('.', '', 1).isdigit() and '.' in x]
strings = [x for x in data if not x.isdigit() and not x.replace('.', '', 1).isdigit()]
print("Integers:", integers)
print("Floats:", floats)
print("Strings:", strings)
