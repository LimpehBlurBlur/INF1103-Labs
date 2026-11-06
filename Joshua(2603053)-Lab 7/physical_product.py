from product import Product

class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, quantity, weight):
        super().__init__(product_id, name, price, quantity)
        self.__weight = weight

    def display_product(self):
        super().display_product()
        print("Weight (kg):", self.__weight, "\n==========================================")

    def get_fulfilment_info(self):
        return "Physical Shipping Only!!!."


