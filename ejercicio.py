class Carrito:
    def __init__(self):

        self.items = []


    def calcular_total(self, promo_tipo):
        total = sum(precio for _, precio in self.items)

        if promo_tipo == "BLACK_FRIDAY":
            return total * 0.5
        elif promo_tipo == "SUMMER_SALE":
            return total - 20
        elif promo_tipo == "BUY_2_GET_3":
        # …
            return total
        else:
            return total