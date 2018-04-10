class Register:
    def __init__(self, products):
        self.products = products
        # self.discounts = discounts

    def __str__(self):
        str = ""
        for item in self.products:
            str += item.name + ", "
        return str
