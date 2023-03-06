class CartePizzariaException(Exception):
    pass

class CartePizzeria:
    def __init__(self, pizza):
        self.carte = []
        self.pizza = pizza

    def is_empty(self):
        if len(self.carte) == 0:
            return True
            print("liste vide")
        return False

    def nb_pizzas(self):
        return self.carte

    def add_pizza(self, pizza):
        self.carte.append(pizza)

    def remove_pizza(self, name):
        if name in self.carte:
            self.carte.remove(name)
        raise CartePizzariaException("La pizza n'est pas dans la carte")



