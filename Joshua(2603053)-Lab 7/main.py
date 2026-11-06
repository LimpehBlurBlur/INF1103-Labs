import json
from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from can_be_shipped import CanBeShipped

def load_data(inventory):
    try:
         with open("database.json", "r") as f:
            data = json.load(f)
         for items in data:
             if items["type"]== "physical":
                 product = PhysicalProduct(items["id"], items["name"], items["product_price"],
                                    items["product_qty"], items["weight"])
             elif items["type"]== "digital":
                product = DigitalProduct(items["id"], items["name"], items["product_price"],
                                items["product_qty"], items["download_size"])
             else:
                 continue
             inventory.add_product(product)
    except FileNotFoundError:
         print("Database not found, creating new one....")
         with open('database.json', "w") as file:
            current_inventory=[
            ]
            json.dump(current_inventory,file,indent=4)

def save_data(inventory):
    data=[]
    for product in inventory.get_all_products():
        data.append(product.to_dict())
    with open("database.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Inventory saved!")


def main():
    inventory = Inventory()
    load_data(inventory)
    failed_attempts = 0

    while True:
        print("\n==============Menu=================\n"
              "1) Display All Products\n"
              "2) Add Product\n"
              "3) Update Stock\n"
              "4) Search Product (And applicable shipping cost)\n"
              "5) Save Inventory\n"
              "6) Exit\n"
              "=====================================")
        try:
            next_action = int(input("Enter Option: "))
        except ValueError:
            print("Invalid Input!")
            failed_attempts += 1
            continue

        match next_action:
            case 1:
                inventory.display_inventory()

            case 2:
                try:
                    product_name=input("====================\nProduct name:").strip()
                    product_qty=int(input("Product qty:"))
                    product_price=float(input("Product price (per item):"))
                    product_type=input("====================\nProduct type (physical/digital):").strip().lower()

                   
                    if product_name=="":
                        raise ValueError
                    elif product_qty < 0 or product_price < 0:
                        raise ValueError
                    else:
                         if product_type=="physical":
                            product_weight=float(input("Product weight(kg):"))
                            new_id = len(inventory.get_all_products()) + 1
                            product = PhysicalProduct(new_id, product_name, product_price, product_qty,product_weight)
                         elif product_type=="digital":
                            product_size=float(input("Product size(MB):"))
                            new_id = len(inventory.get_all_products()) + 1
                            product = DigitalProduct(new_id, product_name, product_price, product_qty,product_size)
                         else:
                            raise ValueError  
                    if not inventory.add_product(product):
                        failed_attempts += 1
                
                except ValueError:
                        print("Invalid Input!!!!!")
                        failed_attempts += 1
    

            case 3:
                try:
                    product_id=int(input("====================================\nEnter product ID:"))
                    new_product_name=input("====================\nNew product name:").strip()
                    new_product_qty=int(input("New product qty:"))
                    new_product_price=float(input("New Product price(per item):"))

                    product = inventory.search_product(product_id)
                    if not product:
                        raise ValueError
                    if not product.update_data(new_product_name,new_product_price,new_product_qty):
                        raise ValueError

                except ValueError:
                    print("Invalid Input!")
                    failed_attempts += 1
                    continue
            case 4:
                try:
                    item_id=int(input("====================================\nEnter item ID:"))
                    product= inventory.search_product(item_id)
                    if not product:
                        raise ValueError
                    if isinstance(product, CanBeShipped):
                        print("Shipping cost: $", product.calculate_shipping_cost())
                except ValueError:
                    print("Invalid Input!!!!!")
                    failed_attempts += 1
            case 5:
                save_data(inventory)
            case 6:
                print("Total failed attempts this session:", failed_attempts)
                break
            case _:
                print("Invalid option!")
                failed_attempts += 1


main()