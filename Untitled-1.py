'''class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, mileage, fuel_type):
        super().__init__(brand, model)
        self.mileage = mileage
        self.fuel_type = fuel_type

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Mileage: {self.mileage} km/l, Fuel Type: {self.fuel_type}")

car = Car("Tata", "Nano", 18, "Petrol")
car.display_info()'''

'''class Clock:
    def __init__(self, hour, minute):
            self.hour = hour
            self.minute = minute

class Calendar:
    def __init__(self, day, month, year):
          self.day = day
          self.month = month
          self.year = year

class CalendarClock(Clock, Calendar):
    def __init__(self, hour, minute, day, month, year):
        Clock.__init__(self, hour, minute)
        Calendar.__init__(self, day, month, year)

    def display(self):
        print(f"Date: {self.day}/{self.month}/{self.year}, Time: {self.hour}:{self.minute}")


calendar_clock = CalendarClock(11, 30, 11, 4, 2025)
calendar_clock.display()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number

class Exam(Student):
    def __init__(self, name, age, roll_number, sub1, sub2, sub3):
        super().__init__(name, age, roll_number)
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
    
    def calculate_marks(self):
        total_marks = self.sub1 + self.sub2 + self.sub3
        average_marks = total_marks//3
        return total_marks, average_marks
    
    def display(self):
        total, average = self.calculate_marks()
        print(f"Name: {self.name}, Age: {self.age}, Roll Number: {self.roll_number}")
        print(f"Subject 1: {self.sub1}, Subject 2: {self.sub2}, Subject 3: {self.sub3}")
        print(f"Total Marks: {total}, Average Marks: {average}")

rajesh = Exam("Rajesh", 17, 63, 85, 90, 88)
rajesh.display()

import math
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi*self.radius**2
    def perimeter(self):
        return 2 * math.pi * self.radius
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def perimeter(self):
        return self.a + self.b + self.c
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side**2
    def perimeter(self):
        return 4*self.side
circle = Circle(5)
print(f"Circle - Area: {circle.area():.2f}, Perimeter: {circle.perimeter():.2f}")
triangle = Triangle(3, 4, 5)
print(f"Triangle - Area: {triangle.area():.2f}, Perimeter: {triangle.perimeter():.2f}")
square = Square(4)
print(f"Square - Area: {square.area():.2f}, Perimeter: {square.perimeter():.2f}")'''