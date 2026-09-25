inventory_quantity=0 
failed_inputs=0
#while true loop creates infinity loop

while True:
    #get user quantity input
    user_input=input("-------------------\nInventory Counter\n-------------------\n*Type 'Quit' to end process\nEnter quantity: ").strip();
    if user_input.lower()=="quit":
        break;


   #check if input is a valid poistive integer 
    if user_input.isdigit() != True:
        print("Enter valid integers only!")
        failed_inputs+=1
    else:    
        inventory_quantity+=int(user_input)
        if inventory_quantity > 500:
            print("inventory quantity exceeded 500!")
            break; 


print("-------------------\nTotal units processed:",inventory_quantity ,"\nTotal failed inputs:" ,failed_inputs)


    
