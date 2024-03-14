def multiply_digits(num):
    number_1 = 1
    while num >= 9:
        digits = [int(digit) for digit in str(num)]
        number_1 = 1
        for digit in digits:
            number_1 *= digit
        num = number_1
    return number_1

user_input = int(input("Please enter a number: "))
result = multiply_digits(user_input)
print(result)
