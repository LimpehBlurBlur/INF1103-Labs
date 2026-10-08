import json





def usermenu(current_inventory):
    failed_attempts=0
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
                            "=====================================\n" \
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
        case _:
            failed_attempts+= 1
            print("Invalid input, try again!!!")




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
    product_id=input("====================================\nEnter product ID:")
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
        total_cost+= x['cost']
    tax=total_cost*0.1

    print("Total tax: $" , tax ,
          "\nTotal failed items this session: " , failed_attempts)



def load_data():
    try:
        with open('database.json','r') as f:
            current_inventory=json.load(f)
            return current_inventory

    except FileNotFoundError:
        print("af")
        with open('database.json', "w") as file:
            current_inventory=[
            ]
            json.dump(current_inventory,file,indent=4)

            pass





    filename='test.txt'
    inventory_list=[]
    saved_qty=0


    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    data = line.split(":")
                    inventory_list.append(data)
                    data[2]=int(data[2])
                    saved_qty+=data[2]
        
                    
    except FileNotFoundError:
        #creates file if it does not exist
        with open(filename, "w") as file:
            pass
    

    if session_list:
        inventory_list.extend(session_list)
        return inventory_list,saved_qty
        
    else:
        return inventory_list,saved_qty

def save_inventory(inventory_list):
    filename="test.txt"
    with open(filename, "w") as file:
        for item_id, product, qty in inventory_list:
            file.write(f"{item_id}:{product}:{qty}\n")
    print("--------------------------------------------------------------\nENTRIES SAVED!")
   



    print("------------------------------\nCurrent inventory stock:")

    if inventory_list:
        last_id = int(inventory_list[-1][0])
        for item_id, product, qty in inventory_list:
            print(f"{item_id} : {product} : {qty}")
    else:
        print("Inventory is currently empty...")
        last_id= 0

    return last_id
    
def cache_list(last_id,item, quantity,session_list):
    last_id+=1
    session_list.append([last_id, item,quantity])
    return last_id,session_list
    


def get_valid_input():
    #prompts user
    item_input=input("-------------------\nInventory Counter\n-------------------\n*Type 'Quit' to end process and save data\nEnter item name: ").strip();

    #check user typed quit
    if item_input.lower()=="quit":
        check="shutdown"
        f_attemmpt=0
        return check ,f_attemmpt , 0 , None
    
    quantity_input=input("Enter quantity: ").strip();

    #check if user typed quit when prompted for qty
    if quantity_input.lower()=="quit" or quantity_input.lower()=="quit":
        check="shutdown"
        f_attemmpt=0
        return check ,f_attemmpt , 0 , None

    #check if valid input
    elif quantity_input.isdigit() != True:
        print("Invalid input! Only integers!")
        check="continue"
        f_attemmpt= 1
        return check,f_attemmpt, 0 , None
    
    #add quantity into the 'register'
    else:
        quantity=int(quantity_input)
        item=item_input
        check="continue"
        f_attemmpt= 0
        return check,f_attemmpt,quantity,item

    #this process function just += the existing num and new num
def process_delivery(current_total, new_value):
    return current_total+new_value

#this x 0.1 (10%)
def calculate_tax(inventory_quantity):
    return inventory_quantity *0.1

def generate_report(total_fattempts, inventory_quantity,tax_amount):
    print("--------------------------------------------------------------\nTotal units processed this session:",inventory_quantity ,"\nTotal tax enquired this session  :" ,tax_amount,"\nTotal failed inputs this session:" ,total_fattempts)

def json_write(current_inventory):
    with open('database.json', 'w') as f:
        json.dump(current_inventory,f)

##########################################################################SEPERATE MAIN FUNC FROM SUB FUNC############################################################################################################################################################################################################################################




def main():
    #establish variables
    total_fattempts=0
    inventory_quantity=0
    tax_amount=0


    #create a loop
    while True: 
        current_inventory=load_data ()

        usermenu(current_inventory)


        #validates inputs and send results of validation
        status, f_attempts, quantity,item= get_valid_input()

       
        total_fattempts+= f_attempts

        #if status from prev function = shutdown, user has typed quit. (is this considered hardcoded?)
        if status == "shutdown":
            generate_report(total_fattempts, inventory_quantity,tax_amount)
            break
        #else if input is a valid nuber, it is proccessed


        elif quantity != 0:

            #calls the process function
            inventory_quantity = process_delivery(inventory_quantity, quantity)

            #calls the calculate tax function and add on the new amount to the existing
            tax_amount += calculate_tax(quantity)
            #rounds value to 2 dec place
            tax_amount=round(tax_amount,2)

            #check if inventory is above 500 , if it does still generate a report but end the code 
            if inventory_quantity > 500:
                print("-------------------\nWARNING!\nTotal units exceeded 500, items entered not saved! Please try again!")
                break


main()




    
