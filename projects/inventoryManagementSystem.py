inventory = {}
id = 1
while True:
    choice = int(input("Choose an option: \n1. Add product\n2. Search product\n3. Update product\n4. Sell product\n5. Delete product\n6. Display all products\n7. Show total inventory value\n8. Exit\n"))

    match choice:
        case 1:
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            if price<=0:
                print("Price should be greater than 0")
            else:
                quantity = int(input("Enter quantity: "))
                if quantity <=0:
                    print("Quantity should be greater than 0")
                else:    
                    inventory[id] = [name,price,quantity]
                    print("Product added.\nId: ",id )
                    id+=1

        case 2:
            searchId = int(input("Enter id: "))
            if searchId in inventory:
                    print("Product name: ",inventory[searchId][0],"\nPrice: ",inventory[searchId][1],"\nQuantity: ",inventory[searchId][-1])
            else:
                print("Item is not in inventory.")

        case 3:
            updateId = int(input("Enter id: "))
            if updateId in inventory:
                newPrice = float(input("Enter new price: "))
                if newPrice<=0:
                    print("Price should be greater than 0")
                else:
                    inventory[updateId][1] = newPrice    
                    newQuantity = int(input("Enter quantity: "))
                    if newQuantity<=0:
                        print("Quantity should be greater than 0")
                    else:
                        inventory[updateId][-1] = newQuantity
            else:
                print("Item is not in inventory.")

        case 4:
            sellId = int(input("Enter id: "))
            if sellId in inventory:           
                print("Price: ", inventory[sellId][1])
                print("Quantity available: ", inventory[sellId][-1]) 
                qSell = int(input("Enter quantity: "))
                if qSell <=0:
                    print("Quantity should be greater than 0")
                elif qSell> inventory[sellId][-1]:
                    print("Not enough stock")
                else:
                    amount = inventory[sellId][1] * qSell
                    print("Cost: ",amount)
                    inventory[sellId][-1] -= qSell
            else:
                print("Item is not in inventory.")

        case 5: 
            delId = int(input("Enter id: "))
            if delId in inventory:
                del inventory[delId]
            else:
                print("Item is not in inventory.")

        case 6:
            for id in inventory:
                print("Id: ",id ,"\nName: ",inventory[id][0],"\nPrice: ",inventory[id][1], "\nQuantity: ",inventory[id][-1])

        case 7: 
            totalValue = 0
            for items in inventory:
                totalValue+= inventory[items][1]*inventory[items][-1]
            print("Total value: ",totalValue)
        case 8:
            break

        case _:
            print("Invalid input.")



            

