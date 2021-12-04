"""i = 10
while i >= 0:
    print(i)
    i -= 1"""
"""
i = 0
list = [1,2,3,4,5,6,7,True]
while i < len(list):
    print(list[i])
    i += 1"""
"""count = 0
while input("Type a message").lower() != "stop":
    print(count)
    count += 1"""
"""list = []
i = 0
another_number = True
while another_number:
    answer = input("Do you want another number?: ").lower()
    if answer == "stop":
        another_number = False
    elif answer == "yes":
        list.append(i)
        i += 1
        print(list)
    elif answer == "two":
        list.extend([i,i+1])
        print(list)
        i+=1
    else:
        print("It is not defined")
        another_number = False"""

list1 = [[1,2,3],[4,5,6],[7,8,9]]
print(list1[0][0])





