import abc
from abc import ABC,abstractmethod

class animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class dog(animal):
    def sound(self):
        print('dog barks')
class cat(animal):
    def sound(self):
        print('cat meow')
    

obj1=dog()
obj2=cat()

obj1.sound()
obj2.sound()