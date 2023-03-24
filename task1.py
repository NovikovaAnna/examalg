# TODO Оценить асимптотическую сложность приведенного ниже алгоритма:
a = len(arr) - 1
out = list()
while a > 0:
    out.append(arr[a])
    a = a // 1.7
out.merge_sort()

"Cложность алгоритма зависит от сложности каждого из этапов \
Данный алгоритм состоит из двух основных этапов: \
Цикл while, который выполняется до тех пор, пока переменная a не станет меньше или равной 0.\
Внутри цикла выполняются операции добавления элемента в конец списка и деление переменной a на 1.7.\
Сложность цикла while зависит от количества итераций. Количество итераций: O(log(arr)). \
В каждой итерации выполняются операции добавления элемента в список и деление переменной a на 1.7.  \
Деление занимает O(1), а добавление элемента в список - O(1) в среднем случае,\
но O(n) в худшем случае, если список требует перевыделения памяти.\
В этом случае суммарная сложность добавления n элементов в список будет O(n^2).\
Однако вероятность такого случая довольно мала, поэтому в среднем случае сложность добавления элемента будет O(1)."