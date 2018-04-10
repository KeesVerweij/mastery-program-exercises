from product import Product
from register import Register
from customer import Customer

p1 = Product(1, 'Washing powder', 8)
p2 = Product(2, 'Chocolate', 2)
p3 = Product(3, 'Chinese veggies', 3)
p4 = Product(4, 'Yoghurt', 1.50)
p5 = Product(5, 'Butter', 2.50)

product_catalog = [p1, p2, p3, p4, p5]
register = Register(product_catalog)
print(register)

shopping_cart = {p2: 2, p4: 5, p1: 3}
customer = Customer(shopping_cart)
print(customer)
print(customer.get_receipt())
