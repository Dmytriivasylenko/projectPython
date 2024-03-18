def time_1(seconds):
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    if days == 1:
        days_str = "день"
    elif 2 <= days <= 4:
        days_str = "дні"
    else:
        days_str = "днів"

    time_str = f"{int(days)} {days_str}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
    return time_str

def input_seconds():
    while True:
        try:
            seconds = int(input("введіть число більше або дорівнює 0 і менше ніж 8640000.):"))
            if seconds >= 0 and seconds <= 8640000:
                return seconds
            else:
                print("Неправильне значення!Введіть число більше або дорівнює 0 і менше ніж 8640000.")
        except ValueError:
            print("Будь ласка, введіть ціле число.")

seconds =input_seconds()

print(f"Формат часу: {time_1(seconds)}") #результат