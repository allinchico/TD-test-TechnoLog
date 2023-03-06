class CartePizzeria:
    def __init__(self, pizza):
        self.carte = []
        self.pizza = pizza

    def is_empty(self):
        if len(self.carte) == 0:
            return True
        return False

    def nb_pizzas(self):
        return self.carte

    def add_pizza(self, pizza):
        self.carte.append(pizza)

    def remove_pizza(self, name):
        self.carte.remove(name)
