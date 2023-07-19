class Expense:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def meth(self):
        ...

    def __add__(self, other):
        return self.cost + other.cost

food = Expense('Food', 50)
fuel = Expense('Fuel', 20)

print(food + fuel)

