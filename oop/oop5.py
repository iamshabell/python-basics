

class SoftwareEngineer:
    def __init__(self):
        self._salary = None
    
   
    # getter
    @property
    def salary(self):
        return self._salary
    # setter
    @salary.setter
    def salary(self, value):
        # check constraints, calculation
        self._salary = value

    # @salary.deleter
    # def salary(self):
    #     self._salary 
    
se = SoftwareEngineer()
se.salary = 6000

# del se.salary
print(se.salary)


# Recap:
# encapsulation
# asbtraction
# public and private
# _foo(), _x
# getter / setter
# getter -> @property
# setter -> x.setter