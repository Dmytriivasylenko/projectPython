def split_list(input_list):
    if len(input_list) == 0:
        return [[], []]
    elif len(input_list) % 2 == 0:
        split_index = len(input_list) // 2
    else:
        split_index = len(input_list) // 2 + 1

    first_half = input_list[:split_index]
    second_half = input_list[split_index:]
    return [first_half, second_half]






















