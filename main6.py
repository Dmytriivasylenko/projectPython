def my_list(lst):
    if not lst:
        return 0

    sum_1 = sum(lst[i] for i in range(0, len(lst), 2))
    result = sum_1 * lst[-1]

    return result

print(my_list([0, 1, 7, 2, 4, 8]))
print(my_list([1, 3, 5]))
print(my_list([6]))
print(my_list([]))
