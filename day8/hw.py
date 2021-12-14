def find(list_,num_):
    for num in list_:
        if num == num_:
            return [True,list_.index(num)]
    return False
    
print(find([1,2,3,4,5],1))