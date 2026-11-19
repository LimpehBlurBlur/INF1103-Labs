from product import Product

class Inventory:
    def __init__(self):
        self.__product=[]

    def add_product(self,product:int) -> bool:
        self.__product.append(product)
        return True
        
    def display_inventory(self) -> None:
        for x in self.__product:
            x.display_product()

    def search_product(self,product_id:int) ->Product | None:
        for item in self.__product:
            if item.get_product_id()==product_id:
                item.display_product()
                return item
        print("Item not found!")
        return False

    def get_all_products(self) -> list[Product]:
      return self.__product

    def find_product(self, product_id: int)-> Product | None:
        for item in self.__product:
            if item.get_product_id()==product_id:
                return item
        return None

    def remove_product(self,product_id: int) -> Product | None:
        product=self.find_product(product_id)
        if product is None:
            return None
        self.__product.remove(product)
        return product
        



