number = int(input("Введіть 5-ти значне число: "))

reversed_number = (number % 10) * 10000 + ((number // 10) % 10) * 1000 + ((number // 100) % 10) * 100 + ((number // 1000) % 10) * 10 + ((number // 10000) % 100)

print("Зворотнє число:", reversed_number)
