# with open('weather_data.csv') as file:
#     f1 = file.readlines()
#     f1_new = []
#     for item in f1:
#         item = item.rstrip()
#         item = item.split(',')
#         f1_new.append(item)
#     print(f1_new)

# import csv
#
# with open('weather_data.csv') as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas
#
# data = pandas.read_csv('weather_data.csv')
# print(data)
# print('\n')
# print(data['temp'])