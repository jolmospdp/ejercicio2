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

class Product():
    def __init__(self, name: str, price: float):
        if price <= 0:
            raise ValueError("El precio debe ser mayor a cero")
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add(self, product: Product):
        self.__items.append(product)

    def calcular_total(self, promotion:Promotion = None):
        total = sum(product.get_price() for product in self.__items)
        if promotion:
            return promotion.apply(total)
        return total

p1 = Product("Juguete", 28000)
p2 = Product("Camisa", 65000)
p3 = Product("Xiaomi redmi note 14 pro plus", 1300000)

shopping_cart = ShoppingCart()
shopping_cart.add(p1)
shopping_cart.add(p2)
shopping_cart.add(p3)

print("Total del carrito sin descuento:")
print(shopping_cart.calcular_total())
print("Aplicando descuento de Navidad:")
print(shopping_cart.calcular_total(Christmas()))
print("Aplicando descuento de BackFriday:")
print(shopping_cart.calcular_total(BlackFriday()))
print("Aplicando descuento de Verano:")
print(shopping_cart.calcular_total(SummerSale()))