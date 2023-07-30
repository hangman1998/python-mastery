class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def __str__(self) -> str:
        return f"{self.name:10} {self.shares:10} {self.price:10.2f}"


google = Stock("GOOG", 10, 342.2)
print(google)
