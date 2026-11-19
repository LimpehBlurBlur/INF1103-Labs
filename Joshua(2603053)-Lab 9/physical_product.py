from product import Product
from can_be_shipped import CanBeShipped
from supplier import Supplier

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id:int , name:str , price:float , quantity:int, weight:float, suppplier: Supplier):
        super().__init__(product_id, name, price, quantity, suppplier)
        self.__weight = weight

    def display_product(self)-> None:
        super().display_product()
        print("Weight (kg):", self.__weight, "\n==========================================")

    def get_fulfilment_info(self) -> str:
        return "Physical Shipping Only!!!."

    def calculate_shipping_cost(self)->float:
        return self.__weight*2

    def to_dict(self)->dict:
        data= super().to_dict()
        data["type"]="physical"
        data["weight"]= self.__weight
        return data


