"""def sum(x,y):   
    return x + y
print(sum(2,3))
print(sum(-2,10))
"""

def max(a,b):
    return a > b
    '''if a>b:
        return True
    else:
        return False'''


print(type(max(2,5)))


x = int(input("Type a number:"))
y = int(input("Type another number: "))
if max(x,y):
    print("First number is bigger than second")
elif not max(x,y):
    print("Second number is bigger tha first")