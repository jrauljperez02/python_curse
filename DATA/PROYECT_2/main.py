import pandas

data = pandas.read_csv('weather_day.csv')
print(type(data))


data_dict = data.to_dict()
#print(data_dict)


#to access to a  columm
data_temp = data['temp'].to_list()
#print(data_temp)

#first way
#print(data['temp'].mean())

#second way
#print(sum(data_temp) / len(data_temp))

#find the biggest value in data_temp
#print(data['temp'].max())


#temp = data['temp']
#print(type(temp))

#print('--------------------------------')

friday = data[data.day == 'Friday']
friday_temp = (friday.temp * (9/5)) + 32

#print(friday_temp)


data_dict_2 = {'students':['Raul','Sofia','Ana','Alberto'],
               'Grades':[9.0,9.2,8.7,7.9]}
data = pandas.DataFrame(data_dict_2)
data.to_csv('grades.csv')


