class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}")
obj1 = Student("Pulak", 60, 91)
obj1.display()
obj2 = Student("Jessica", 36, 87)
obj2.display()