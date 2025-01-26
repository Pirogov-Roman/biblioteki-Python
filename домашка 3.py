import numpy as np
import pandas as pd

# 1. Привести различные способы создания объектов типа Series
# array1 = np.array([1,2,3,4,5])
# data1 = pd.Series(array1 )
# print(data1)
# dict2 = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'd': 1,
# }
# data2 = pd.Series(dict2)
# print(data2)
# data3 = pd.Series([1,2,3,4,5])
# print(data3)
# data4 = pd.Series(3, index=['a', 'b', 'c', 'd'])
# print(data4)



# 2. Привести различные способы создания объектов типа DataFrame
# ser1 = pd.Series([1,2,3], index=['row1', 'row2', 'row3'])
# ser2 = pd.Series([4,5,6], index=['row1', 'row2', 'row3'])
# data1 = pd.DataFrame({'A': ser1, 'B': ser2})
# print(data1)

# list_dict = [
#     {'name': 'Alla', 'age': 25, 'city': 'Samara'},
#     {'name': 'Sergey', 'age': 13, 'city': 'Saint-Petersburg'},
#     {'name': 'Ivan', 'age': 21, 'city': 'Paris'}
# ]
# data2 = pd.DataFrame(list_dict)
# print(data2)

# array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# data3 = pd.DataFrame(array, columns=['col1', 'col2', 'col3'], index=['row1', 'row2', 'row3'])
# print(data3)

# structured_array = np.array(
#     [('Alla', 25, 'Samara'), ('Sergey', 13, 'Spb'), ('Ivan', 21, 'Paris')],
#     dtype=[('name', 'U10'), ('age', 'i4'), ('city', 'U15')]
# )
# data4 = pd.DataFrame(structured_array)
# print(data4)

# s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
# s2 = pd.Series([4, 5, 6], index=['a', 'b', 'c'])
# data5 = pd.DataFrame([s1, s2])
# print(data5)




# 3. Объедините два объекта Series с неодинаковыми множествами ключей (индексов) так, чтобы вместо NaN было установлено значение 1
# pop = pd.Series({
#     'city 1': 1001,
#     'city 2': 1002,
#     'city 3': 1003,
#     'city 41': 1004,
#     'city 52': 1005,
# })

# area = pd.Series({
#     'city 1': 9991,
#     'city 2': 9992,
#     'city 3': 9993,
#     'city 42': 9994,
#     'city 50': 9995,
# })

# data = pd.DataFrame({'area1': area, 'pop1': pop}).fillna(1)
# print(data)


# 4. Переписать пример с транслированием для DataFrame так, чтобы вычитание происходило не по строкам, а по столбцам
# data = pd.DataFrame({
#     'A': [10, 20, 30],
#     'B': [40, 50, 60],
#     'C': [70, 80, 90]
# })

# subtract_series = pd.Series([5, 10, 15], index=['A', 'B', 'C'])
# result = data.subtract(subtract_series, axis=1)
# print(result)



# 5 На примере объектов DataFrame продемонстрировать использование методов ffill() и bfill()
# data = pd.DataFrame({
#     'A': [1, None, 3, None, 5],
#     'B': [None, 2, None, 4, None],
#     'C': [25, None, None, 50, None]
# })
# print(data)

# # ffill()
# ffill_result = data.ffill()
# print(ffill_result)

# # bfill()
# bfill_result = data.bfill()
# print(bfill_result)