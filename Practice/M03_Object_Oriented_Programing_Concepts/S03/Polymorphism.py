
def add(a,b,c,d):
    return a+b+c+d

print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))

"""'pyton does not support function overloading directly
 we can achieve this using variable-length arguments(using *)'"""

def add(*value):
    return sum(values)

print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40)) 

#module in Abstraction
#ABC-abstract base class->abstract methods