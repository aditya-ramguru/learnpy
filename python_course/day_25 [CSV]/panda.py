import pandas

data = pandas.read_csv('weather_data.csv')
# print(data)
# print('\n')

# templist = data['temp'].to_list()
# average_temp = sum(templist)/len(templist)
# print('%0.2f'%average_temp)
# print(round(average_temp,3))

# print(templist)
# data_dict = data.to_dict()
# print(data_dict)

# print(data['temp'].mean())
# x = data.temp.max()
# print(x)

#  to get data from row
# print(data[data.day == 'Monday'])
# print('\n')
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == 'Monday']
# temp = monday.temp
# temp = (temp*9)/5 + 32
# print(temp)

# Create dataframe from scratch
data_dict = {
    'students': ['angela','aditya','arya'],
    'scores': [98, 99, 100]
}

data = pandas.DataFrame(data_dict)
print(data)

data.to_csv('new_data.csv')