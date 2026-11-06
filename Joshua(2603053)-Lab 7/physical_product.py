from product import Product
from can_be_shipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, quantity, weight):
        super().__init__(product_id, name, price, quantity)
        self.__weight = weight

    def display_product(self):
        super().display_product()
        print("Weight (kg):", self.__weight, "\n==========================================")

    def get_fulfilment_info(self):
        return "Physical Shipping Only!!!."

    def calculate_shipping_cost(self):
        return self.__weight*2

    def to_dict(self):
        data= super().to_dict()
        data["type"]="physical"
        data["weight"]= self.__weight
        return data


