import numpy as np
import sys
import array

# Типы данных Python

# x = 1
# print (type(x))
# print (sys.getsizeof(x)) #размер в байтах 

# x = 'hello'
# print (type(x))

# x = True
# print (type(x))

# список
# l1 = list([])
# print(sys.getsizeof(l1))

# l2 = list([1, 3, 5])
# print(sys.getsizeof(l2))

# l3 = list([1, '2', True])
# print(l3)

# массив
# a1 = array.array('i', [1,2,3]) # i это код типа - значит что мы кладем числа инт в массив
# print(sys.getsizeof(a1))
# print(type(a1))




# Numpy
# a = np.array([1,2,3,4,5])
# print(type(a), a)

# # повышающее приведение типов
# a = np.array([1.23, 2, 3, 4, 5]) #нампи попытается привести все элементы к одному типу(в данном случаю к float)
# print(type(a), a)

# a = np.array([-1.23, 2, 3, 4, 5], dtype = 'int') # если хотим конкретный тип установить, то указываем к какому именно хотим привести
# print(type(a), a) # тогда произойдет округление(отбрасывается дробная часть в данном случае)

# a = np.array([range(i,i+3) for i in [2,4,6]])
# print(a, type(a))

# a = np.zeros(10, dtype='int') # массив из нулей
# print(a, type(a))

# print(np.ones((2,4), dtype='float')) # массив из единиц

# print(np.full((4,5), 3.1415)) # заполнение конкретными значениями

# print(np.arange(0, 20, 2)) # последовательность чисел (полезно для графиков)

# print(np.eye(4)) # получение квадратной единичной матрицы конкретного размера

# в двумерных массивах сначала идут строки, потом столбцы



### МАССИВЫ
 
np.random.seed(1) # установка начального значения

# x1 = np.random.randint(10, size=3)
# x2 = np.random.randint(10, size=(3,2)) # двумерный массив из случайных чисел
# x3 = np.random.randint(10, size=(2,3,1)) # n-мерное пространство можем задавать
# print(x2)
# print(x3)

# print(x1.ndim, x1.shape, x1.size) #1 число размерности, 2 размер каждой размерности, 3 общий размер массива
# print(x2.ndim, x2.shape, x2.size)
# print(x3.ndim, x3.shape, x3.size)

# Индекс (с 0)
# a = np.array([1,2,3,4,5])
# print(a[-2])

# a[1] = 20

# a = np.array([[1,2],[3,4]])
# print(a[0,0])

# a[-1,-1] = 100
# print(a)

# a = np.array([1,2,3,4])
# b = np.array([1.0,2,3,4])

# print(a)
# print(b)
# a[0] = 10
# print(a)
# a[0] = 10.123
# print(a) # число будет приведено к инту все равно

## Срез [start:end:step] [0;shape:1] - по умолчанию

# a = np.array([1,2,3,4,5,6])
# print(a[:3]) # первые три элемента
# print(a[3:])
# print(a[1:-1])
# print(a[1::2])
# print(a[::-1]) # выводится массив в обратном порядке



#cрезы это не копии массивов, они ссылаются на тот массив, где производится срез
# a = np.array([1,2,3,4,5,6])
# b = a[:3]
# print(b)
# b[0] = 100
# print(a) # произойдет замена на 100 все равно

# 8 задача: написать код как сделать срез-копию

# a = np.arange(1, 13)
# print(a)
# print(a.reshape(2,6)) # превратится в 2 строчки по 6 элементов. ОБЯЗАТЕЛЬНО СООТВЕТСВИЕ РАЗМЕРНОСТЕЙ

# 9 задача: newaxis продемонстрировать использование его для получения вектора-столбца и вектора-строки из массива

# x = np.array([1,2,3])
# y = np.array([4,5])
# z = np.array([6])
# print(np.concatenate([x,y,z])) # объединение массивов

# x = np.array([1,2,3])
# y = np.array([4,5,6])

# r1 = np.vstack([x,y]) # вертикальное склеивание
# print(r1)
# print(np.hstack([r1,r1])) #[[1 2 3 1 2 3] горизонатльное склеивание
#                           # [4 5 6 4 5 6]]


### Вычисления с массивами
# Веткоризированная операция - независимо к каждому элементу массива

# x = np.arange(10)
# print(x)
# print(x*2 + 1)

# # универсальные функции 

# print(np.add(np.multiply(x,2),1))

# - -(унарный) / // ** %



# np.abs, sin, cos, tan, exp, log, и т.д.

# x = np.arange(5)
# y = np.empty(10) # можно нулевой через zeros 
# print(np.multiply(x, 10, out=y[::2])) #результат запишется в у (можно без среза если размерности совпадают)

# x = np.arange(1,5)
# print(x) # [1 2 3 4]
# print(np.add.reduce(x)) # 10
# print(np.add.accumulate(x)) # [1 3 6 10] то есть поэтапно записываются как складывались

x = np.arange(1,10)
print(np.add.outer(x,x)) #таблица сложения для чисел от 1 до 10. Аналогично можно таблицу умножения
