'''
Polymorphism is an OOP concept where a single function, method, or operator behaves differently based on the
 context (object type or input).

The word "Polymorphism" means many forms.

polymorphism can be achieved in 4 ways 

Duck Typing	                            Method  behaves differently based on object passed
Operator Overloading                    Same operator behaves differently for different data types
Method Overriding	                    Subclass overrides method of superclass
Function Overloading (not built-in) 	Can be mimicked using default/variable arguments
'''

import multipledispatch 
from multipledispatch import dispatch

#1. Duck typing -- Python cares about the methods, not the object's type.

class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

def animal_sound(animal):
    animal.speak()

animal_sound(Dog())  # Output: Bark
animal_sound(Cat())  # Output: Meow

#2.Method Overriding--A subclass overrides a method defined in its parent class.

class Vehicle:
    def start(self):
        print("Vehicle starting")

class Car(Vehicle):
    def start(self):
        print("Car starting")

v = Vehicle()
v.start()  # Output: Vehicle starting

c = Car()
c.start()  # Output: Car starting


#3.Operator Overloading--Same operator behaves differently for different types.

print(5 + 10)      # Output: 15 (int)
print("a" + "b")   # Output: ab (str)

class Book:
    def __init__(self, pages):
        self.pages = pages
    
    def __add__(self, other):
        return Book(self.pages + other.pages)

b1 = Book(100)
b2 = Book(150)
b3 = b1 + b2
print(b3.pages)  # Output: 250

#4.Method overloading -- method overloading can not be achieved in the traditional python but we 
#achieve by default or arbitary or multiple dispatch 

#default 
def greet(name=None):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello!")

greet()         # Output: Hello!
greet("Ram")    # Output: Hello, Ram!

# arbitary 

def add(*args):
    return sum(args)

print(add(1, 2))          # Output: 3
print(add(1, 2, 3, 4))    # Output: 10

#multiple dispatch 

class overload:
    @dispatch(int,int)
    def add(self,a,b):
        return a+b 
    @dispatch(str,str)
    def add(self,a,b):
        return a+b

o1=overload()
print(o1.add(2,3))
print(o1.add('vamshi','dar'))

 