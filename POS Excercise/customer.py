class Customer:
    def __init__(self, products):
        self.products = products

    def get_receipt(self):
        total = 0
        for item in self.products:
            total += item.price * self.products[item]
        return "total: " + str(total)

    def pay():
        '''
        pays the cashier the requested amount
        '''
        pass

    def __str__(self):
        output = ""
        for item in self.products:
            output += item.name + ": " + str(self.products[item]) + ", "
        return output
