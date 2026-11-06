from product import Product

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, quantity, download_size):
        super().__init__(product_id, name, price, quantity)
        self.__download_size=download_size

    def display_product(self):
        super().display_product()
        print("Download size (MB):", self.__download_size ,"\n==========================================")

    def get_fulfilment_info(self):
        return "Online download Only!!!."

    def to_dict(self):
        data= super().to_dict()
        data["type"]="digital"
        data["download_size"]=self.__download_size
        return data





