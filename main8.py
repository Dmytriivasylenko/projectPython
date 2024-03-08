import string
import keyword
def variable_name(name):
    if name[0].isdigit():
        return False
    if name.isdigit():
        return False
    if name in keyword.kwlist:
        return False
    for char in name:
        if char not in string.ascii_letters + string.digits + "_":
            return False
    return True

#ПРИКЛАДИ
test_cases = ['_', 'x', 'get_value', 'get value', 'get!value', 'some_super_puper_value', 'Get_value', 'get_Value',
              'getValue', '3m', 'm3']
for name in test_cases:
    print(f"{name} => {variable_name(name)}")
