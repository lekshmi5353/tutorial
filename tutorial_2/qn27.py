def custom_sort(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

numbers = list(map(int, input("Enter a list of numbers: ").split()))
sorted_list = custom_sort(numbers)
print("Sorted list:", sorted_list)
