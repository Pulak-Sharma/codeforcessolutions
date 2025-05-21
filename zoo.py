from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Lion(Animal):
    def make_sound(self):
        print("Roar")
class Elephant(Animal):
    def make_sound(self):
        print("Trumpet")
class Monkey(Animal):
    def make_sound(self):
        print("Chatter")

def make_all_sounds(animals):
    for animal in animals:
        animal.make_sound()
zoo = [Lion(), Elephant(), Monkey()]
make_all_sounds(zoo)
