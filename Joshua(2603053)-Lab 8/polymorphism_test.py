from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory

supplier = Supplier(1, "Music World Pte Ltd", "sales@musicworld.com")
guitar = PhysicalProduct(1, "Guitar", 300.0, 5, 4.5, supplier)
software = DigitalProduct(2, "Music Mixer Pro", 49.90, 100, 350, supplier)


shop = Inventory()
shop.add_product(guitar)
shop.add_product(software)


print("===== POLYMORPHISM TEST =====")
for product in shop.get_all_products():
    product.display_product()
    print(product.get_fulfilment_info())
