# Příklad 3: Základy OOP (dědičnost, abstrakce, zapouzdření)
# Zadání:
# Vytvořte dvě podtřídy třídy `Shape`: `Rectangle` a `Circle`.
# - `Rectangle` má atributy `width` a `height` a implementuje metodu `area`.
# - `Circle` má atribut `radius` a implementuje metodu `area`.


class Shape():

    def area(self):
        return 0.0

class Rectangle(Shape):
    
    def __init__(self, vyska, sirka):
        self.height = vyska
        self.width = sirka

    def area(self):
        return  self.height * self.width

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2


from unittest.mock import patch, MagicMock, mock_open

# Pytest testy pro Příklad 3
def test_shapes():
    rect = Rectangle(4, 5)
    assert rect.area() == 20

    circle = Circle(3)
    assert round(circle.area(), 1) == 28.3

