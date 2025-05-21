class Arithmetic:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self, a, b):
        print(a+b)
    def subtract(self, a, b):
        print(a-b)
    def multiply(self, a, b):
        print(a*b)
    def divide(self, a, b):
        if b==0:
            print("Division by zero is not possible")
        else:
            print(a/b)
obj1 = Arithmetic(5,0)
obj1.add(45,6)
obj1.subtract(0,5)
obj1.divide(5,0)
obj1.multiply(5,10)

class Arithmetic():
    def __init__(self,a,b):
        self.a = a
        self.b = b
        

#obj = class()
obj1 = Arithmetic()
