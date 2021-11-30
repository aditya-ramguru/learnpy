import pandas

data = pandas.read_csv('Squirrel_Data.csv')

color = data['Primary Fur Color'].to_list()
d = {}
for item in color:
    if (type(item)) == str:
        d[item] = d.get(item, 0) + 1
# d = {k : v for k, v in d.items() if k == k}
print(d)

new = {
    'Fur color' : [key for key in d],
    'Count' : [d[key] for key in d]
}

# data_frame = pandas.DataFrame(new)
# print(data_frame)
# data_frame.to_csv('squirrel_color_count.csv')
