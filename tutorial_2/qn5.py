string = input("Enter a string: ")
odd_indices = ''.join(string[i] for i in range(len(string)) if i % 2 != 0)
even_indices = ''.join(string[i] for i in range(len(string)) if i % 2 == 0)
print("Odd indices:", odd_indices)
print("Even indices:", even_indices)
