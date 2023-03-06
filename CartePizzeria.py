class CartePizzariaException(Exception):
    pass

class CartePizzeria:
    def __init__(self):
        self.carte = []
       
    def is_empty(self):
        if len(self.carte) == 0:
            print("La liste est vide")
            return True
        return False

    def nb_pizzas(self):
        return len(self.carte)

    def add_pizza(self, pizza):
        self.carte.append(pizza)

    def remove_pizza(self, name):
        if name in self.carte:
            self.carte.remove(name)
        raise CartePizzariaException("La pizza n'est pas dans la carte")



