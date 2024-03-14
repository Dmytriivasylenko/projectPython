import string
def format_1(input_str):
    start, end = input_str.split('-')
    letters = string.ascii_letters
    start_index = letters.index(start)
    end_index = letters.index(end)
    return letters[start_index:end_index+1]
input_str = input("Enter two letters separated by a hyphen: ")
print(format_1(input_str))





