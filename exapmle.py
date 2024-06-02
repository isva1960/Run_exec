# Лучше присвоивать значения, а не вводить
# Если для ввода используем input, то необходимо делать вывод в консоль

# Пример 1
# Значения присваиваются
a = 1
b = 2
x = 0
for i in range(1, 4):
    x = x + a * i + b
    print(f'Промежуточный результат: {i=}, {x=}')
print(f'Конечный результат: {x=}')

# Пример 2
# Вывод в консоль
# Значения вводим с помощью input
a = int(input('Введите a: '))
print(f'{a=}')
b = int(input('Введите b: '))
print(f'{b=}')
x = 0
for i in range(1, 4):
    x = x + a * i + b
    print(f'Промежуточный результат: {i=}, {x=}')
print(f'Конечный результат: {x=}')

# Пример 3
# Без вывода в консоль, используем QInputDialog
# Значения вводим с помощью QInputDialog
from PyQt5.QtWidgets import QInputDialog

a, ok = QInputDialog.getInt(self, '', 'Введите a:')
print(f'{a=}')
b, ok = QInputDialog.getInt(self, '', 'Введите b:')
print(f'{b=}')
x = 0
for i in range(1, 4):
    x = x + a * i + b
    print(f'Промежуточный результат: {i=}, {x=}')
print(f'Конечный результат: {x=}')

# Пример 4
# Средне арифметическое
# Значения присваиваются
numbers = [4, 8, 6, 5, 3, 2]
average = sum(numbers) / len(numbers)
print(average)

# Пример 5
# Средне геометрическое
# Значения присваиваются
import statistics

numbers = [4, 8, 6, 5, 3, 2]
g_mean = statistics.geometric_mean(numbers)
print(g_mean)

# Пример 6
# Значения присваиваются
from math import *

print(sin(pi))  # в радинах
print(sin(radians(90)))  # в градусах

# Пример 7
# Без вывода в консоль, используем QInputDialog
# Значения вводим с помощью QInputDialog
from PyQt5.QtWidgets import QInputDialog

name, ok = QInputDialog.getText(self, '', 'Введите имя:')
print(f'Привет, {name}!')
