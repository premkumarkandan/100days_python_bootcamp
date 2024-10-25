# data = []
# with open('weather_data.csv', 'r') as file:
#     data = file.readlines()
#
# print(data)
import csv

# with open('weather_data.csv', 'r') as file:
#     data = csv.reader(file)
#     temperatures = []
#     # print(data)
# #
#     for value in data:
#         # print(value[1])
#         if value[1] != 'temp':
#             temperatures.append(int(value[1]))
#     print(temperatures)

import pandas
import numpy as np

data = pandas.read_csv('weather_data.csv')
# print(data['temp'])
#
# temp_dict = data.to_dict()
# print(temp_dict)
#
# temp_list = data['temp'].to_list()
# print(temp_list)

# ans1 = np.mean(temp_list)  # method 2 using numpy inbuilt function
series = pandas.Series(data['temp'])  # method 3 using pandas inbuilt fn
# ans3 = series.mean()
# ans4 = series.max()
# print(data.temp)
# print(ans)
# print(ans1)
# print(ans3)
# print(type(data['temp']))
# print(type(data))
print(data[data.temp == data.temp.max()])  # just column name works
monday = data[data.day == 'Monday']
f = (monday.temp * 9/5) + 32
print(f)
