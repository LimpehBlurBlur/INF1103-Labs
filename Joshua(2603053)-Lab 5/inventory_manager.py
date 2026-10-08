import json


def usermenu(current_inventory,failed_attempts):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" \
            "INVENTORY MANAGEMENT SYSTEM \n" \
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    try:
        next_action=int(input("\n==============Menu=================\n" \
                                "1)Display All Products\n" \
                                "2)Add Products\n" \
                                "3)Update Stock\n" \
                                "4)Search Product\n" \
                                "5)Delete Item\n" \
                                "6)Save Session and quit"
                                "\n=====================================" \
                                "\nEnter Option:"))
    except ValueError:
        print("Invalid Input!!!!!")
        failed_attempts += 1
        return True,failed_attempts

    match next_action:
        case 1:
            display_inventory(current_inventory)
        case 2:
            current_inventory,failed_attempts=add_data(current_inventory,failed_attempts)
        case 3:
            current_inventory,failed_attempts=update_data(current_inventory,failed_attempts)
        case 4:
            failed_attempts=search_data(current_inventory,failed_attempts)
        case 5:
            current_inventory,failed_attempts=del_data(current_inventory,failed_attempts)
        case 6:
            save_inventory(current_inventory,failed_attempts)
            return False , failed_attempts
        case _:
            failed_attempts+= 1
            print("Invalid input, try again!!!")
    return True,failed_attempts




def add_data(current_inventory,failed_attempts):
    try:
        product_name=input("====================\nProduct name:").strip()
        product_qty=int(input("Product qty:"))
        product_price=int(input("Product price (per item):"))
        total_qty = 0
        for x in current_inventory:
            total_qty+=int(x["product_qty"]) 
        qty_check=total_qty+product_qty

        if product_name=="":
            raise ValueError
        elif product_qty < 0 or product_price < 0:
            raise ValueError
        elif qty_check > 500:
            print("Total inventory exceeded 500!")
            raise ValueError
        
    except ValueError:
        print("Invalid Input!!!!!")
        failed_attempts += 1
        return current_inventory,failed_attempts
   



    total_product_price=product_qty * product_price
    if len(current_inventory) ==0:
        current_id=0
    else:
        current_id=current_inventory[-1]["id"]
        print(current_id)
        current_id=int(current_id)

    new_dict={"id": current_id+1, "name":product_name , "product_qty":product_qty ,"product_price":total_product_price }
    current_inventory.append(new_dict)
    return current_inventory,failed_attempts
    



def display_inventory(current_inventory):
    for x in current_inventory:
        print("==========================================\nID:",x['id'], "\nItem:", x['name'], "\nQuantity:",x['product_qty'], "\nPrice($):",x['product_price'],"\n==========================================")

def update_data(current_inventory,failed_attempts):
    display_inventory(current_inventory)
    try:
        product_id=int(input("====================================\nEnter product ID:"))
        new_product_name=input("====================\nNew product name:").strip()
        new_product_qty=int(input("New product qty:"))
        new_product_price=int(input("New Product price(per item):"))
        
        

        if new_product_name=="":
            raise ValueError
        elif new_product_qty < 0 or new_product_price < 0 :
            raise ValueError
        elif product_id < 1 or product_id > len(current_inventory):
            raise ValueError
        else:
            total_qty = 0
            for x in current_inventory:
                total_qty+=int(x["product_qty"])
            qty_check=total_qty-int(current_inventory[product_id-1]["product_qty"])+new_product_qty

            if qty_check > 500 :
                print("Quanity too much !!!")
                raise ValueError
        
    except ValueError:
        print("Invalid Input!!!!!")
        failed_attempts += 1
        return current_inventory,failed_attempts


    total_new_product_price=new_product_price*new_product_qty
    target_product=int(product_id)-1
    current_inventory[target_product]={"id":product_id, "name":new_product_name , "product_qty":new_product_qty,"product_price":total_new_product_price}
    return current_inventory,failed_attempts


def search_data(current_inventory,failed_attempts):
    try:
        item_id=int(input("====================================\nEnter item ID:"))
    except ValueError:
        print("Invalid Input!!!!!")
        failed_attempts += 1
        return failed_attempts

    for item in current_inventory:
        if item_id == item["id"]:
            print("ID:", current_inventory[item_id-1]["id"],
                  "\nItem:", current_inventory[item_id-1]["name"],
                  "\nQuantity:", current_inventory[item_id-1]["product_qty"],
                  "\nPrice($):", current_inventory[item_id-1]["product_price"])
    return failed_attempts

def del_data(current_inventory,failed_attempts):
    try:
        del_id=int(input("====================================\nEnter item ID to delete:"))
        target_id=del_id-1

        if del_id < 1 or del_id > len(current_inventory):
            raise ValueError
    except ValueError:
        print("Invalid Input!!!!!")
        failed_attempts += 1
        return current_inventory,failed_attempts

    del current_inventory[target_id]

    x=1
    for items in current_inventory:
        items['id'] =x
        x+=1
    return current_inventory,failed_attempts
    

def save_inventory(current_inventory,failed_attempts):
    with open('database.json', 'w') as f:
        json.dump(current_inventory,f)
    generate_report(current_inventory,failed_attempts)


def generate_report(current_inventory,failed_attempts):
    display_inventory(current_inventory)
    total_cost=0
    for x in current_inventory:
        total_cost+= int(x['product_price'])
    tax=total_cost*0.1

    print("Total tax: $" , tax ,
          "\nTotal failed items this session: " , failed_attempts)



def load_data():
    try:
        with open('database.json','r') as f:
            current_inventory=json.load(f)
            return current_inventory

    except FileNotFoundError:
        print("Database not found, creating new one....")
        with open('database.json', "w") as file:
            current_inventory=[
            ]
            json.dump(current_inventory,file,indent=4)
            return current_inventory






#ef json_write(current_inventory):
#   with open('database.json', 'w') as f:
#       json.dump(current_inventory,f)

##########################################################################SEPERATE MAIN FUNC FROM SUB FUNC############################################################################################################################################################################################################################################




def main():
    #create a loop
    current_inventory=load_data()
    failed_attempts=0
    while True: 
        continue_program,failed_attempts=usermenu(current_inventory,failed_attempts)

        if continue_program:
            pass
        elif continue_program == False:
            break


main()




    
