while True:
    number1 = float(input("Please enter first number: "))
    number2 = float(input("Please enter second number: "))
    action = input("Please enter action (+, -, *, /): ")

    if action == '+':
        result = number1 + number2
    elif action == '-':
        result = number1 - number2
    elif action == '*':
        result = number1 * number2
    elif action == '/':
        if number2 != 0:
            result = number1 / number2
        else:
            print("You can't divide by 0")
            continue
    else:
        print("Invalid action")
        continue

    print("Your result is", result)
    break
