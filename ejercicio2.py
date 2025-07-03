from abc import ABC, abstractmethod

class Promotion(ABC):
    @abstractmethod
    def apply(self,total:float)->float:
        pass

class Christmas(Promotion):
    def apply(self,total:float)->float:
        return total - (total*0.10)

class BlackFriday(Promotion):
    def apply(self, total: float) -> float:
        return total * 0.5

class SummerSale(Promotion):
    def apply(self, total: float) -> float:
        return total - (total*0.20)


class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add(self, product, price):
        self.__items.append((product,price))

    def calcular_total(self, promotion:Promotion = None):
        total = sum(precio for _, precio in self.__items)
        if promotion:
            return promotion.apply(total)
        return total


shopping_cart = ShoppingCart()
shopping_cart.add("Juguete", 28000)
shopping_cart.add("Camisa", 65000)
shopping_cart.add("Xiaomi redmi note 14 pro plus", 1300000)

print("Total del carrito sin descuento:")
print(shopping_cart.calcular_total())
print("Aplicando descuento de Navidad:")
print(shopping_cart.calcular_total(Christmas()))
print("Aplicando descuento de BackFriday:")
print(shopping_cart.calcular_total(BlackFriday()))
print("Aplicando descuento de Verano:")
print(shopping_cart.calcular_total(SummerSale()))