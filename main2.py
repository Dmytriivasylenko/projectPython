def calculator():
    while True:
        try:
            num1 = float(input("Please enter first number: "))
            num2 = float(input("Please enter second number: "))
            action = input("Please enter action (+, -, *, /): ")
        if action == "+":
            result = num1 + num2
        elif action == "-":
            result = num1 - num2
        elif action == "*":
            result = num1 * num2
        elif action == "/":
            result = num1 / num2
            if num2 == 0:
                print("You can't dived by 0")
                continue
            else:
                result = num1 / num2
        else:
            print("Invalid action")
            continue

        print("Your result is" result)
        break
except ValueError:
        print("Please enter valid numbers")
calculator()