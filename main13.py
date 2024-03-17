def time_1(seconds):
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return f"{days} {'day' if days == 1 else 'days'}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

user_input = int(input("Enter the number of seconds: "))

if 0 <= user_input < 8640000:
    result = time_1(user_input)
    print("Time in a readable format:", result)
else:
    print("The entered number does not match the task conditions.")
