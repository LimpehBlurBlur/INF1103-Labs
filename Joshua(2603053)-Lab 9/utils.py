import csv
from inventory import Inventory
from supplier import Supplier
from product_factory import ProductFactory


def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number, e.g. 12.50")

def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    loaded = 0
    try:
        file = open(path, newline="")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        with file:
            reader = csv.reader(file)
            next(reader)                      
            for row in reader:
                try:
                    product_type, product_id, name, price, quantity = row
                    product = ProductFactory.create(product_type, product_id, name,
                                                    float(price), int(quantity), supplier)
                    inventory.add_product(product)
                    loaded += 1
                except ValueError as error:
                    print(f"Skipped row {row}: {error}")
        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")