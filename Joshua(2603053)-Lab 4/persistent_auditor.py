def load_inventory(session_list):
    filename='test.txt'
    inventory_list=[]


    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    data = line.split(":")
                    inventory_list.append(data)
                    
    except FileNotFoundError:
        #creates file if it does not exist
        with open(filename, "w") as file:
            pass
    

    if session_list:
        inventory_list.extend(session_list)
        return inventory_list
    else:
        return inventory_list
        
def display_inventory(inventory_list):
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
    item_input=input("-------------------\nInventory Counter\n-------------------\n*Type 'Quit' to end process\nEnter item name: ").strip();
    quantity_input=input("Enter quantity: ").strip();
    #check user typed quit
    if item_input.lower()=="quit" or quantity_input.lower()=="quit":
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
    print("-------------------\nTotal units processed:",inventory_quantity ,"\nTotal tax:" ,tax_amount,"\nTotal failed inputs:" ,total_fattempts)


######################################################################################################################################################################################################################################################################################################################

def main():
    #establish variables
    total_fattempts=0
    inventory_quantity=0
    tax_amount=0
    session_list=[]

    #create a loop
    while True: 

        #load lists 
        inventory_list=load_inventory(session_list) 

        #display lists 
        last_id=display_inventory(inventory_list)
        
        #validates inputs and send results of validation
        status, f_attempts, quantity,item= get_valid_input()

       

        total_fattempts+= f_attempts

        #if status from prev function = shutdown, user has typed quit. (is this considered hardcoded?)
        if status == "shutdown":
            generate_report(total_fattempts, inventory_quantity,tax_amount)
            break
        #else if input is a valid nuber, it is proccessed
        elif quantity != 0:
             #save entries into the session list until program quits and save it
            last_id,session_list=cache_list(last_id,item, quantity,session_list)
            #calls the process function
            inventory_quantity = process_delivery(inventory_quantity, quantity)
            #calls the calculate tax function and add on the new amount to the existing
            tax_amount += calculate_tax(quantity)
            #rounds value to 2 dec place
            tax_amount=round(tax_amount,2)

            #check if inventory is above 500 , if it does still generate a report but end the code 
            if inventory_quantity > 500:
                generate_report(total_fattempts, inventory_quantity,tax_amount)
                print("Total units exceeded 500, please reset!")
                break

 
       

                
                



   
        #   inventory_quantity+=int(user_input)
        #   if inventory_quantity > 500:
        #       print("inventory quantity exceeded 500!")
        #       break; 

main()




    
