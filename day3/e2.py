import random
names_string = input("Give all the names (separated by ','): ")
names_list = names_string.split(",")
print(names_list)
print(names_list[random.randint(0,len(names_list))])



