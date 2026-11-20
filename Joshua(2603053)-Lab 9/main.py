import json
from inventory import Inventory
from can_be_shipped import CanBeShipped
from supplier import Supplier
from product_factory import ProductFactory
from order import Order
from discount_strategy import NoDiscount, PercentageDiscount, BulkDiscount, StudentDiscount
from utils import get_positive_float, load_products

def load_data(inventory: Inventory)-> None:
    try:
         with open("database.json", "r") as f:
            data = json.load(f)
         for items in data:
             s = items["supplier"]
             supplier = Supplier(s["id"], s["name"], s["email"])
             
             if items["type"] == "physical":
                extra = items["weight"]
             else:
                extra = items["download_size"]

             product = ProductFactory.create(items["type"], items["id"], items["name"],items["product_price"], items["product_qty"], supplier, extra)
             inventory.add_product(product)


    except (FileNotFoundError, json.JSONDecodeError):
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
              "6) Create Customer Order\n"
              "7) Receive new Stock Batch (from csv file)\n"
              "8) Exit\n"
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
                    product_price = get_positive_float("Product price (per item):")
                    product_type=input("====================\nProduct type (physical/digital):").strip().lower()
                    supplier_id = input("Supplier Short UEN (etc 345A): ").strip().upper()
                    supplier_name = input("Supplier name: ").strip()
                    supplier_email = input("Supplier email: ").strip()

                    if supplier_id == "" or supplier_name == "" or supplier_email == "":
                        raise ValueError
                
                    if product_name=="":
                        raise ValueError
                    elif product_qty < 0 or product_price < 0:
                        raise ValueError
                    else:
                         supplier = Supplier(supplier_id, supplier_name, supplier_email)
                         if product_type=="physical":
                            extra =float(input("Product weight(kg):"))
                         elif product_type=="digital":
                            extra =float(input("Product size(MB):"))
                         else:
                            raise ValueError  
                    new_id = len(inventory.get_all_products()) + 1
                    product = ProductFactory.create(product_type, new_id, product_name, product_price, product_qty, supplier, extra)
                    inventory.add_product(product)
                
                except ValueError as error:
                        print("Invalid Input!!!!!", error)
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
                    product.update_data(new_product_name, new_product_price, new_product_qty)

                except ValueError as error:
                    print("Invalid Input!", error)
                    failed_attempts += 1
                    continue
            case 4:
                try:
                    item_id=int(input("====================================\nEnter item ID:"))
                    product= inventory.search_product(item_id)
                    if not product:
                        raise ValueError
                    product.get_supplier().display_information()
                    if isinstance(product, CanBeShipped):
                        print("Shipping cost: $", product.calculate_shipping_cost())
                except ValueError:
                    print("Invalid Input!!!!!")
                    failed_attempts += 1
            case 5:
                save_data(inventory)
            case 6:
                print("Discount: 1) None  2) 10% off  3) $20 off $200+  4) Student 5%")
                choice = input("Choose discount:").strip()
                if choice == "2":
                    discount = PercentageDiscount(10)
                elif choice == "3":
                    discount = BulkDiscount(200, 20)
                elif choice == "4":
                    discount = StudentDiscount()
                elif choice == "1":
                    discount = NoDiscount()
                else:
                    print ("No valid option chose, no dicount applied")
                    discount = NoDiscount()

                order = Order(1001, discount)
                while True:
                    text = input("Product ID to add (enter 'done' to end):").strip()
                    if text == "done":
                        break
                    try:
                        product = inventory.find_product(int(text))
                        if product is None:
                            print("Item not found!")
                            continue
                        order.add_order_line(product, int(input("Quantity:")))
                    except ValueError as error:
                        print("Invalid Input!", error)
                order.display_order()

            case 7:
                supplier_id = input("Supplier Short UEN (etc 345A): ").strip().upper()
                supplier_name = input("Supplier name: ").strip()
                supplier_email = input("Supplier email: ").strip()
                batch_supplier = Supplier(supplier_id, supplier_name, supplier_email)

                load_products("products.csv", inventory, batch_supplier)
                save_data(inventory)
            case 8:
                print("Total failed attempts this session:", failed_attempts)
                break

            case _:
                print("Invalid option!")
                failed_attempts += 1


if __name__ == "__main__":
    main()