# Single	One parent → one child	A → B
# Multiple	Multiple parents → one child	A + B → C
# Multilevel	Grandparent → Parent → Child	A → B → C
# Hierarchical	One parent → multiple children	A → B, C
# Hybrid	Combination of inheritance types	A → B,C → D


#Single Inheritance
class Parent:
    def show_parent(self):
        print("This is the Parent class")
class Child(parent):
    def show_child(self):
        print("This is Child class")
obj=Child()
obj.show_parent()
object.show_child()


#Multiple Inheritance
class Father:
    def father_property(self):
        print("Father's property")


class Mother:
    def mother_property(self):
        print("Mother's property")


class Child(Father, Mother):
    def child_property(self):
        print("Child's property")


obj = Child()

obj.father_property()
obj.mother_property()
obj.child_property()

#Multilevel inheritance
class Grandparent:
    def grandparent_method(self):
        print("Grandparent class")


class Parent(Grandparent):
    def parent_method(self):
        print("Parent class")


class Child(Parent):
    def child_method(self):
        print("Child class")


obj = Child()

obj.grandparent_method()
obj.parent_method()
obj.child_method()


#Hybrid
class A:
    def method_a(self):
        print("Class A")


class B(A):
    def method_b(self):
        print("Class B")


class C(A):
    def method_c(self):
        print("Class C")


class D(B, C):
    def method_d(self):
        print("Class D")


obj = D()

obj.method_a()
obj.method_b()
obj.method_c()
obj.method_d()

#python does not support overloading- because it passes different arguments,
#same method,different arguments
#Duck typing is a feature of Python where the type or class of an object is less important than the methods or behavior that the object provides
# Remember 🦆
# “If it walks like a duck and quacks like a duck, treat it like a duck.”
# That's the basic idea of duck typing.
class Dog:
    def sound(self):
        print("Dog says Woof")
class Cat:
    def sound(self):
        print("Cat says Meow")
def make_sound(animal):
    animal.sound()
dog = Dog()
cat = Cat()
make_sound(dog)
make_sound(cat)

#type checking:
x = 10
print(type(x))

name = "Nikhitha"
print(type(name))

#isinstance
#isinstance() is used to check whether an object belongs to a particular data type or class.
#isinstance(object, type)-> syntax
x = 10
print(isinstance(x, int))
print(isinstance(x, str))


# Polymorphism is one of the major concepts of Object-Oriented Programming (OOP).
# The word comes from:
# Poly → many
# Morph → forms
# So, polymorphism means “one thing having many forms.”
# In Python, polymorphism allows us to use the same method, function, or operator with different objects, while each object can behave differently.

# Imagine you have a method called:
# make_sound()
# Different animals make different sounds:
# Dog → Woof
# Cat → Meow
# Cow → Moo


# Same method + different implementation = Method overriding polymorphism