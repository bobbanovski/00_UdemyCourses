
class Checkout:
    class Discount:
        def __init__(self, numItems, price):
            self.numItems = numItems
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}
        # self.total = 0

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        # self.total += self.prices[item]
        if item not in self.prices:
            raise Exception
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculateTotal(self):
        # return self.total
        total = 0
        for item, cnt in self.items.items():
            total += self.calculateItemTotal(item, cnt)
        return total

    def addDiscount(self, item, numItems, price):
        discount = self.Discount(numItems, price)
        self.discounts[item] = discount

    def calculateItemTotal(self, item, cnt):
        total = 0
        # If item is a discount item
        if item in self.discounts:
            # If number of items added >= number required for discount
            discount = self.discounts[item]
            if cnt >= discount.numItems:
                num_discounts = cnt / discount.numItems
                total += num_discounts * discount.price
                # Get number of items that discount does not apply to
                remaining = cnt % discount.numItems
                total += remaining * self.prices[item]
            else:
                # Apply normal pricing
                total += self.prices[item] * cnt
        else:
            total += self.prices[item] * cnt
        return total
