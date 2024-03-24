def common_elements():
    multiples_of_3 = [num for num in range(3, 31) if num % 3 == 0]
    multiples_of_5 = [num for num in range(5, 51) if num % 5 == 0]
    common_set = set(multiples_of_3) & set(multiples_of_5)
    return common_set
print(common_elements())
