def move_last_to_first(input_list):
    if len(input_list) > 1:
        input_list.insert(0, input_list.pop())
    return input_list