class Price:
    def __init__(self, part_number, price):
        self.price = price
        self.part_number = part_number

    def get_price(self):
        return  self.price


instance=Price("pitter", 1.39)

print (f"the current price of {instance.part_number} is  {instance.get_price()}")

def function__init__(self, part_number, price):
        self.price = price
        self.part_number = part_number


def function_get_price(self):
        return  self.price    

namespace = {"__init__":function__init__,"get_price":function_get_price}

Price2 = type('Price2', (), namespace)

instance2 = Price("patter", 7.65)
print (f"the current price of {instance2.part_number} is  {instance2.get_price()}")

print(f"instance type is {type(instance)} id {id(instance)}")
print(f"instance2 type is {type(instance2)} id {id(instance2)}")