print(f"____\n Define Price calls\n _______")

class Price:
    def __init__(self, part_number, price):
        self.price = price
        self.part_number = part_number

    def get_price(self):
        return  self.price

print(f"____\n Create item_price instance\n_______")

item_price=Price("pitter", 1.39)

print(f"____\n Compare Class to Instance\n____")

print()
print(f"Price.__dict__ \n{Price.__dict__}")
print()
print(f"item_price.__dict__ \n{item_price.__dict__}")
print()
print(f"dir(Price) \n{dir(Price)}")
print()
print(f"dir(item_price) \n{dir(item_price)}")

print(f"____\n____ define set_discount and get_discount_price\n____")

def set_discount(item_price, percent_off):
    item_price.percent_off = percent_off

def get_discount_price( item_price):
    return item_price.price - item_price.price * item_price.percent_off/100

print(f"____\n____ check out functions\n____")
print(f"")
print()
print(f"set_discount.__dict__ \n{set_discount.__dict__}")
print(f"dir(set_discount) \n{dir(set_discount)}")
print(f"id(set_discount)\n{id(set_discount)}")
print(f"get_discount_price.__dict__ \n{get_discount_price.__dict__}")
print(f"dir(get_discount_price) \n{dir(get_discount_price)}")
print(f"id(get_discount_price)\n{id(get_discount_price)}")

print(f"____\n____ test functions\n____")

set_discount(item_price, 3)
print(f"item_price price is {item_price.price}")
print(f"item_price percent_off is {item_price.percent_off}")
print(f"item_price discount price is {get_discount_price(item_price)}")

print("____ adding functions to class _______")
Price.set_discount = set_discount
Price.get_discount_price = get_discount_price
print("____ now try instance method _______")
item_price.set_discount( 5)
print(f"item_price price is {item_price.price}")
print(f"item_price percent_off is {item_price.percent_off}")
print(f"item_price discount price is {get_discount_price(item_price)}")
print("monkey patch works just like it was originally part of class")

print(f"____\n____ Compare Class to Instance II \n____")

print()
print(f"Price.__dict__ \n{Price.__dict__}")
print()
print(f"item_price.__dict__ \n{item_price.__dict__}")
print()
print(f"dir(Price) \n{dir(Price)}")
print()
print(f"dir(item_price) \n{dir(item_price)}")

print(f"____\n____ add function to instance \n____")
item_price.instance_set_discount = set_discount
item_price.instance_get_discount_price = get_discount_price

item_price.instance_set_discount(item_price,50)
print(f"item_price price is {item_price.price}")
print(f"item_price percent_off is {item_price.percent_off}")
print(f"item_price discount price is {item_price.instance_get_discount_price(item_price)}")
print("It works. adding to instance requires passing instance for self ex: item_price.instance_set_discount(item_price,50)")

print(f"____\n____ Compare Class to Instance III \n____")

print()
print(f"Price.__dict__ \n{Price.__dict__}\n")
print(f"item_price.__dict__ \n{item_price.__dict__}\n")
print(f"dir(Price) \n{dir(Price)}\n")
print(f"dir(item_price) \n{dir(item_price)}\n")
