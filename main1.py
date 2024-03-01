number = int(input("Введіть 5-ти значне число: "))

reversed_number = (number % 10) * 10000 + ((number // 10) % 10) * 1000 + ((number // 100) % 10) * 100 + ((number // 1000) % 10) * 10 + ((number // 10000) % 100)
print("Зворотнє число:", reversed_number)







umber_1 = int((input("Please enter first number: ")))



num2 = float(input("Please enter second number: "))

print ('Приветствуем вас в калькуляторе Python')
q1 = int (input('Введите число 1: '))
q2 = int (input('Введите число 2: '))

v = int (input('Какую операцию вы хотите выполнить? \n 1 Сложение \n 2 Вычитание \n 3 Деление \n 4 Умножение \n'))

if v == 1:
    r = q1 + q2
    p = 'сложения'
    t = p
if v == 2:
    r = q1 - q2
    l = 'вычитания'
    t = l
if v == 3:
    r = float(q1 / q2)
    m = 'деления'
    t = m
if v == 4:
    r = q1 * q2
    n = 'умножения'
    t = n
print ('Результат ',t,' = ',r)
















break
operation = input("Please enter action (+, -, *, /): ")
if action == "+" :
result = num1 + num2
elif action == "-":
result = num1 - num2
elif action == "*":
result = num1 * num2
elif action == "/":
result = num1 / num2
if num2 == 0:
print("You can't dived by 0")
print()rint("Your result is" result)
