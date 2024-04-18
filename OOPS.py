#lets start with class

class Person:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary





    def getsalary(self):
        return self.salary



rohan= Person("Rohan", "35000")
print(rohan.salary)
print(rohan.name)

Abhineet= Person("Abhineet", "3500000")
print(Abhineet.salary)
print(Abhineet.name)
