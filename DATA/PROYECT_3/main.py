import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')


red = 0
black = 0
gray = 0
other = 0


for color in data['Primary Fur Color']:
    if color == 'Gray':
        gray += 1
    elif color == 'Cinnamon':
        red += 1
    elif color == 'Black':
        black += 1
    else:
        other += 1

color_dict = {'color':['Gray','Black','Cinnamon','Other'],
              'Number':[gray,black,red,other]}

final = pandas.DataFrame(color_dict)
final.to_csv('colors1.csv')


#second way
black_squirrels = len(data[data['Primary Fur Color'] ==  'Black'])
red_squirrels = len(data[data['Primary Fur Color'] ==  'Cinnamon'])
gray_squirrels = len(data[data['Primary Fur Color'] ==  'Gray'])


color_dict_2 = {'color':['Gray','Black','Cinnamon'],
              'Number':[gray_squirrels,black_squirrels,red_squirrels]}

final_2 =  pandas.DataFrame(color_dict_2)
final_2.to_csv('colors2.csv')





