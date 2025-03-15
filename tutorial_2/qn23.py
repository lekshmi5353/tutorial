from collections import Counter

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
frequency = Counter(numbers)
mode = [key for key, val in frequency.items() if val == max(frequency.values())]
print("Mode(s):", mode)
