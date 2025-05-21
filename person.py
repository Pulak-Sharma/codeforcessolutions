from datetime import date
class Person:
    name = input()
    dateofbirth = input()
    def calculate_age(self):
        today = date.today()  
        dob_date = date.fromisoformat(self.dateofbirth)  
        age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
        print(age) 

obj1 = Person()
obj1.calculate_age()
