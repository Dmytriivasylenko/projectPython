#ДЗ7.Перемістити всі нулі до кінця списку
#[0, 1, 0, 12, 3] -> [1, 12, 3, 0, 0]
#[0] -> [0]
#[1, 0, 13, 0, 0, 0, 5] -> [1, 13, 5, 0, 0, 0, 0]
#[9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]

def move_zero(lst):
    non_zeros = [x for x in lst if x != 0]
    zeros = [0] * (len(lst) - len(non_zeros))
    return non_zeros + zeros

print(move_zero([0, 1, 0, 12, 3]))
print(move_zero([0]))
print(move_zero([1, 0, 13, 0, 0, 0, 5]))
print(move_zero([9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0,]))