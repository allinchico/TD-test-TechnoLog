from mock import Mock
import unittest
from CartePizzeria import CartePizzeria

class TestCartePizzeria(unittest.TestCase):

    def setUp(self):
        self.pizza = Mock()
        self.carte_vide = CartePizzeria()
        self.carte_non_vide = CartePizzeria()
        self.carte_non_vide.carte = [self.pizza]

    def test_is_empty(self):
        self.assertEqual(self.carte_vide.is_empty(), True)
        
    def test_is_not_empty(self):
        self.assertEqual(self.carte_non_vide.is_empty(), False)

    def test_nb_pizzas_empty(self):
        self.assertEqual(self.carte_vide.nb_pizzas() == 0)

    def test_nb_pizzas_not_empty(self):
        self.assertEqual(self.carte_non_vide.nb_pizzas() == 1)

    def test_add_pizza(self):
        self.carte_vide.add_pizza(self.pizza)
        self.assertEqual(self.carte_vide.carte, [self.pizza])
    
    def test_remove_pizza(self):
        self.carte_non_vide.remove_pizza(self.pizza)
        self.assertEqual(self.carte_non_vide.carte, [])
    
        
        

    


