class Product:
    def __init__(self,product_id,name,price,quantity):
        self.__product_id = product_id
        self.__name=name
        self.__price=price
        self.__quantity=quantity

    def display_product(self):
        print("==========================================")
        print("ID:",self.__product_id)
        print("Item:",self.__name)
        print("Quantity:", self.__quantity)
        print("Price per item($):", self.__price)
        print("==========================================")

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

    



