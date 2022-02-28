

class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type


customers = [
    Customer("caleb", "gold"), Customer('brad', 'bronze')
    
    ]

print(customers[1].name)




