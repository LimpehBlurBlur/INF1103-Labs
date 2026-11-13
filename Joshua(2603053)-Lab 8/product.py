from abc import ABC, abstractmethod
from supplier import Supplier


class Product(ABC):
    def __init__(self,product_id:int ,name:str ,price:float ,quantity:int ,supplier: Supplier):
        self.__product_id = product_id
        self.__name=name
        self.__price=price
        self.__quantity=quantity
        self.__supplier=supplier


    def display_product(self):
        print("==========================================")
        print("ID:",self.__product_id)
        print("Item:",self.__name)
        print("Quantity:", self.__quantity)
        print("Price per item($):", self.__price)

    def update_data(self,name,price,quantity):
        if quantity < 0:
            print("Quantity cannot be negative!")
            return False
        self.__name=name
        self.__price=price
        self.__quantity = quantity
        return True

    def get_product_id(self):
        return self.__product_id

    def get_quantity(self):
        return self.__quantity

    def to_dict(self):
        return {"id": self.__product_id,"name":self.__name,"product_qty": self.__quantity, "product_price": self.__price}

    @abstractmethod
    def get_fulfilment_info(self):
        pass

    def get_supplier(self) -> Supplier:
        return self.__supplier

    def get_price(self) -> float:
        return self.__price

    def get_name(self) -> str:
        return self.__name

    



