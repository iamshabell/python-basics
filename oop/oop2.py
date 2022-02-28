# class
class SoftwareEngineer:
    # class Instance - global
    alias = "Keyboard Magician"

    def __init__(self, name, age, level, salary):
        # instance attributes - only for the object
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
    
    # instance method
    def code(self):
        print(f'{self.name} is coding..')
    
    def code_in_language(self, language):
        print(f'{self.name} is writing code in {language}')

    
    # dunder method
    def __str__(self):
        information = f'name = {self.name}, age ={self.age}, level = {self.level}'
        return information
        
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    
    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000

se1 = SoftwareEngineer("Mubarak", 19, "Junior", 5600)
se2 = SoftwareEngineer("Khalid", 24, "Senior", 8600)
se3 = SoftwareEngineer("Khalid", 24, "Senior", 8600)

se1.code()
se2.code()

se1.code_in_language('Python')
se2.code_in_language('C++')

print(se1.entry_salary(24))

print(SoftwareEngineer.entry_salary(27))

# Recap:
# instances methods(self)
# can take arguments and can return values
# special 'dunder' methods (__str__ and __eq__)
# @staticmethod