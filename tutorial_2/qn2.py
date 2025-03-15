string = input("Enter a string: ")
result = ''.join(string[i] for i in range(len(string)) if i % 2 == 0)
print("String with characters at odd index positions removed:", result)
