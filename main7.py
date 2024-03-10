import random
random_list = []
for _ in range(random.randint(3, 10)):
    random_list.append(random.randint(1, 100))
new_list = [random_list[0], random_list[2], random_list[-2]]

print("list1:", random_list)
print("list2:", new_list)
