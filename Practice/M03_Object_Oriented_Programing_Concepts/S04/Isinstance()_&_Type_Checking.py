# class Animal:
#     pass
# class Dog(Animal):
#     pass
# class cat:
#     pass
# d=Dog()
# c=cat()
# print(isinstance(d,Dog))
# print(isinstance(d,Animal))
# print(isinstance(c,Dog))
# print(isinstance(c,cat))

# #Duck Typing: same method acts as same behaviour, we can use it
# class Dog:
#     def sound(self):
#         print("Bow-Bow")
# class Cat:
#     def sound(self):
#         print("Meow-Meow")
# def make_sound(animal):
#     animal.sound()
# d=Dog()
# c=Cat()
# make_sound(d)
# make_sound(c)


# def process(data):
#     if isinstance(data,int):
#         return data*2
#     elif isinstance(data,int):
#         return data.upper()
#     elif isinstance(data,float):
#         return data*10.5
#     print(process(10))
#     print(process('nikki'))
#     print(process(10.5))

#interview question
class A:
    pass
class B(A):
    pass
obj =B()
print(type(obj)==B)#true
print(type(obj)==A)#false
print(isinstance(obj,B))#true
print(isinstance(obj,A))#true
