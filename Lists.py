from random import randint
from random import uniform
"""Фильтрация чётных чисел
Задача: Дан список целых чисел. Создайте новый список, содержащий только чётные числа, используя цикл или list comprehension.
"""
lst_0 = [randint(-100, 100) for i in range(20)]
lst_0_new = [number for number in lst_0  if (number % 2==0)]

"""
Объединение двух списков с удалением дубликатов
Задача: Даны два списка. Объедините их в один так, чтобы в результирующем списке не было повторяющихся элементов.
"""
lst_1 = [randint(-10, 10) for i in range(20)]
lst_1_new = list(set(lst_0+lst_1))

"""
Поиск максимума и его индекса
Задача: Дана последовательность чисел в списке. Найдите максимальное число и его индекс (если максимум встречается несколько раз — выведите индекс первого вхождения).
"""
lst_0_max_value = max(lst_0)
lst_0_max_value_idx = lst_0.index(max(lst_0))

"""
Переворот списка
Задача: Дан список. Выведите его элементы в обратном порядке, не используя метод reverse() и срезы с шагом -1.
"""
lst_2 = []
for number in range(len(lst_0) - 1, -1, -1):
    lst_2.append(lst_0[number])
print(lst_2)
"""
Генерация списка квадратов
Задача: По данному натуральному числу n создайте список, содержащий квадраты чисел от 1 до n.
"""
n = 10
lst_3 = [i**2 for i in range(1,n+1)]
"""
Подсчёт вхождений элемента
Задача: Дан список строк и заданное слово. Подсчитайте, сколько раз это слово встречается в списке.
"""
lst_4 = ["a","b","c","c","d","d","c","b","s","a"]
word = "a"
word_number = lst_4.count(word)

"""
Удаление дубликатов с сохранением порядка
Задача: Дан список с повторяющимися элементами. Создайте новый список, содержащий только уникальные значения, при этом исходный порядок должен сохраняться.
"""
lst_5 = [randint(-10, 10) for i in range(20)]
lst_5_no_dubles = [number for number in lst_5  if (lst_5.count(number)==1)]
"""
Преобразование элементов списка
Задача: Дан список чисел. Создайте новый список, в котором каждое число делится на 2, а результат округляется до двух знаков после запятой.
"""
lst_6 = [uniform(-10, 10) for i in range(20)]
lst_6_doubled = [round(number/2,2) for number in lst_6 ]

"""
Объединение списков с помощью функции zip
Задача: Даны два списка равной длины. Создайте список кортежей, где каждый кортеж состоит из элементов с одинаковыми индексами из обоих списков.
"""
lst_of_kort = list(zip(lst_0,lst_1))
"""
Удаление отрицательных чисел
Задача: Дан список чисел. Удалите из него все отрицательные элементы и выведите получившийся список."""
lst_0_positive = [number for number in lst_0  if (number>0)]
