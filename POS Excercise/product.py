class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        print(str(self.id) + ", " + self.name + ", " + str(self.price))
