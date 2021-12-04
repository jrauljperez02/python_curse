list1 = [1,2,3,[True,False,"python"]]
#print(list1[3][2])

#Append
list2 = [1,2,3,4]
list2.append("hello")

#Extend
list2.extend([10,11,True,"python"])

#Insert
list2.insert(1,"text")

#Remove
list2.remove(2)

#Pop
list2.pop(1)
print(list2)

#Count
list2.extend([11,11,11])
print(list2.count(11))