#[1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]
#[1, 1, 2, 1] == [1, 2, 2]
#[6, 3, 7] == [6, 7, 3]


import random
def new_list1(input_list):
    new_list = [input_list[0], input_list[2], input_list[-2]]
    return new_list

# Приклади
examples = [
    [1, 2, 3, 4, 5, 6, 7, 9],
    [1, 1, 2, 1],
    [6, 3, 7]
]

for example in examples:
    new_list = new_list1(example)
    print(f"{example} == {new_list}")
