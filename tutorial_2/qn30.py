from collections import Counter

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
frequency = Counter(numbers)
result = [num for num, count in frequency.items() if count == 1]
print("List after removing all duplicate elements:", result)
