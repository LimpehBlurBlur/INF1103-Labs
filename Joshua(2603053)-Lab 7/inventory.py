from product import Product

class Inventory:
    def __init__(self):
        self.__product=[]

    def add_product(self,product):
        total = 0
        for item in self.__product:
            total+= item.get_quantity()

        self.__product.append(product)
        return True
        


    def display_inventory(self):
        for x in self.__product:
            x.display_product()

    def search_product(self,product_id):
        for item in self.__product:
            if item.get_product_id()==product_id:
                item.display_product()
                return item
        print("Item not found!")
        return False

    def get_all_products(self):
      return self.__product



