
def get_valid_input():
    #prompts user
    user_input=input("-------------------\nInventory Counter\n-------------------\n*Type 'Quit' to end process\nEnter quantity: ").strip();
    #check user typed quit
    if user_input.lower()=="quit":
        check="shutdown"
        f_attemmpt=0
        return check ,f_attemmpt , 0

    #check if valid input
    elif user_input.isdigit() != True:
        print("Invalid input! Only integers!")
        check="continue"
        f_attemmpt= 1
        return check,f_attemmpt, 0
    
    #add quantity into the 'register'
    else:
        quantity=int(user_input)
        check="continue"
        f_attemmpt= 0
        return check,f_attemmpt,quantity

    #this process function just += the existing num and new num
def process_delivery(current_total, new_value):
    return current_total+new_value
#this x 0.1 (10%)
def calculate_tax(inventory_quantity):
    return inventory_quantity *0.1

def generate_report(total_fattempts, inventory_quantity,tax_amount):
    print("-------------------\nTotal units processed:",inventory_quantity ,"\nTotal tax:" ,tax_amount,"\nTotal failed inputs:" ,total_fattempts)

def main():
    #establish variables
    total_fattempts=0
    inventory_quantity=0
    tax_amount=0

    #create a loop
    while True: 
        #validates inputs and send results of validation
        status, f_attempts, quantity= get_valid_input()
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
                generate_report(total_fattempts, inventory_quantity,tax_amount)
                print("Total units exceeded 500, please reset!")
                break

 
       

                
                



   
        #   inventory_quantity+=int(user_input)
        #   if inventory_quantity > 500:
        #       print("inventory quantity exceeded 500!")
        #       break; 

main()




    
