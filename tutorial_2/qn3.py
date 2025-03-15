string = input("Enter a string: ")
is_palindrome = all(string[i] == string[-(i+1)] for i in range(len(string) // 2))
print("Palindrome:", is_palindrome)
