from product import Product

class OrderLine:
    def __init__(self, product: Product, quantity: int):
        self.__product: Product=product
        self.__quantity: int=quantity

    def calculate_subtotal(self)->float:
        return self.__product.get_price()*self.__quantity

    def get_product(self)-> Product:
        return self.__product

    def display_line(self)->None:
        print("Product ID:", self.__product.get_product_id(),"(", self.__product.get_name(),") x",self.__quantity, "=", self.calculate_subtotal())