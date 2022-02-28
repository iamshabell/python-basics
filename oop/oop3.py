

# inherits, extend, override
class Employee:
    

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f'{self.name} is working...')

class SoftwareEngineer(Employee):
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    def work(self):
        print(f'{self.name} is coding...')

    def debug(self):
        print(f'{self.name} is debugging...')

class Designer(Employee):
    def work(self):
        print(f'{self.name} is designing...')

    def draw(self):
        print(f'{self.name} is rolling...')


se = SoftwareEngineer("Max", 18, 7000, "junior")
# se.work()
# se.debug() 

des = Designer('Philiph', 27, 8000)
# des.work()
# des.draw()




# Polymorphism

employees = [
    SoftwareEngineer("Max", 18, 7000, "Junior"),
    SoftwareEngineer("Sarah", 20, 8000, "Sunior"),
    Designer('Philiph', 27, 8000)

]
def motivate_employees(employees):
    for employee in employees:
        employee.work()


motivate_employees(employees)

# Recap:
# inheritance: ChildClass(BaseClass)
# inherit, extend, override
# super().__init__()
# polymorphism