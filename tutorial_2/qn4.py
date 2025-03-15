string = input("Enter a string: ")
if ' ' in string:
    result = string.replace(' ', '*')
else:
    result = f"${string}$"
print("Modified string:", result)
