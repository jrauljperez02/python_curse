import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator")
nr_letters = int(input("How many letters would you like your password? "))
nr_numbers = int(input("How many numbers would you like your password? "))
nr_symbols = int(input("How many symbols would you like your password? "))

#easy way
password_string = ""
for _ in range(1,nr_letters +1):
    #password = password + random.choice(letters)
    password_string +=  random.choice(letters)

for _ in range(1,nr_numbers+1):
    password_string += random.choice(numbers)

for _ in range(1,nr_symbols+1):
    password_string += random.choice(symbols)

#print(f"Password:  {password_string}")

#hard way
password_list = []
for _ in range(1,nr_letters + 1):
    password_list.append(random.choice(letters))

for _ in range(1,nr_numbers+1):
    password_list.append(random.choice(numbers))

for _ in range(1,nr_symbols+1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
# [F,1,2,a,s,#]
string_list_password = ''
for element in password_list:
    string_list_password = string_list_password + element

print(string_list_password)




