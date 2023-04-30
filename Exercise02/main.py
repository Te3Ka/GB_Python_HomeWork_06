#\*************************/#
#\*******Te3K@_PaynE*******/#
#\**79811131773@yandex.ru**/#
#\*************************/#

'''
Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
'''
import random

MIN = -100
MAX = 100

# Функция вывода автора программы
def author():
    print('****************************')
    print('Программа создана:')
    print('Илья "Te3K@_PaynE" Новичихин')
    print('79811131773@yandex.ru')
    print('****************************')

def create_random_array(_num, _min, _max):
    _list = []
    for i in range(int(_num)):
        _list.append(random.randint(_min, _max))
    return _list

print("Программа создаёт список из случайных чисел")
print("положительных и отрицательных в диапазоне от -100 до 100")
print("Затем программа выводит индексы тех чисел, которые лежат")
print("между минимумом и максимумом, которые вводит пользователь")
_n = int(input("Введите количество элементов основного массива: "))
_array_original = create_random_array(_n, MIN, MAX)
print(_array_original)
_min = int(input("Введите минимум: "))
_max = int(input("Введите максимум: "))
_array_result = list()
for _i in range(len(_array_original)):
    if _array_original[_i] >= _min and _array_original[_i] <= _max:
        _array_result.append(_i)
print(_array_result)

author()