Реалізуйте генераторну функцію (з використанням оператора yield), яка повертатиме по одному члену числової послідовності, закон якої задається за допомогою функції користувача. Крім цього параметром генераторної функції повинні бути значення першого члена прогресії та кількість членів, що видаються послідовності (n). Генератор повинен зупинити свою роботу з досягнення n-го члена.

Підказка: це завдання дуже схоже на нескінченний лічильник з матеріалів лекції! Потрібно лише обмежити кількість видаваних генератором значень!
def some_gen(begin, end, func):
    for i in range(end):
        yield func(begin)
        begin = func(begin)

from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')