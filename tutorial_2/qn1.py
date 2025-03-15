string = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ''.join(char for char in string if char not in vowels)
print("String without vowels:", result)
