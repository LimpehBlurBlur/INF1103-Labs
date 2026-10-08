import json


def usermenu(current_inventory,failed_attempts):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" \
            "INVENTORY MANAGEMENT SYSTEM \n" \
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    next_action=int(input("\n==============Menu=================\n" \
                            "1)DIsplay All Products\n" \
                            "2)Add Products\n" \
                            "3)Update Stock\n" \
                            "4)Search Product\n" \
                            "5)Delete Item\n" \
                            "6)Save Session and quit"
                            "n\=====================================" \
                            "Enter Option:"))
    match next_action:
        case 1:
            display_inventory(current_inventory)
        case 2:
            current_inventory=add_data(current_inventory)
        case 3:
            current_inventory=update_data(current_inventory)
        case 4:
            search_data(current_inventory)
        case 5:
            current_inventory=del_data(current_inventory)
        case 6:
            save_inventory(current_inventory,failed_attempts)
            return False
        case _:
            failed_attempts+= 1
            print("Invalid input, try again!!!")
    return True




def add_data(current_inventory):
    product_name=input("====================\nProduct name:")
    product_qty=int(input("Product qty:"))
    product_price=int(input("Product price (per item):"))
    total_product_price=product_qty * product_price
    if len(current_inventory) ==0:
        current_id=0
    else:
        current_id=current_inventory[-1]["id"]
        print(current_id)

    new_dict={"id": current_id+1, "name":product_name , "product_qty":product_qty ,"product_price":total_product_price }
    current_inventory.append(new_dict)
    return current_inventory
    



def display_inventory(current_inventory):
    for x in current_inventory:
        print(x['id'], ":|", x['name'], "|x",x['product_qty'], "|",x['product_price'])

def update_data(current_inventory):
    display_inventory(current_inventory)
    product_id=int(input("====================================\nEnter product ID:"))
    new_product_name=input("====================\nNew product name:")
    new_product_qty=int(input("New product qty:"))
    new_product_price=int(input("New Product price(per item):"))
    total_new_product_price=new_product_price*new_product_qty
    target_product=int(product_id)-1
    current_inventory[target_product]={"id":product_id, "name":new_product_name , "product_qty":new_product_qty,"product_price":total_new_product_price}
    return current_inventory


def search_data(current_inventory):
    item_id=int(input("====================================\nEnter item ID:"))
    for item in current_inventory:
        if item_id == item["id"]:
            print(item)

def del_data(current_inventory):
    del_id=input("====================================\nEnter item ID to delete:")
    target_id=int(del_id)-1
    del current_inventory[target_id]

    x=1
    for items in current_inventory:
        items['id'] =x
        x+=1
    return current_inventory
    

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






def json_write(current_inventory):
    with open('database.json', 'w') as f:
        json.dump(current_inventory,f)

##########################################################################SEPERATE MAIN FUNC FROM SUB FUNC############################################################################################################################################################################################################################################




def main():
    #create a loop
    current_inventory=load_data()
    failed_attempts=0
    while True: 
        continue_program=usermenu(current_inventory,failed_attempts)

        if continue_program:
            pass
        elif continue_program == False:
            break


main()




    
