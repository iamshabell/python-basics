

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

se1 = SoftwareEngineer("Mubarak", 19, "Junior", 5600)
se2 = SoftwareEngineer("Khalid", 24, "Senior", 8600)
print(se2.name)

print(se2.alias)


# Recap
# create class (blueprint)
# create a instance (object)
# class vs instance
# instance attributes: defined in __init__(self)
# class attributes