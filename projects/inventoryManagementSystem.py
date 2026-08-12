import csv
def validatePrice(price):
    while price <= 0:
            price = float(input("Enter price greater than 0"))
    return price
def validateQuantity(q):
    while q<= 0:
            q = int(input("Enter quantity greater than 0"))
    return q

def addProduct():
    id = 1
    try:
        with open("inventory.csv" , "r") as file:
            reader = csv.reader(file)
            for line in reader:
                if int(line[0]) >= id:
                    id = int(line[0]) + 1
    except FileNotFoundError:
                    pass
    
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    price = validatePrice(price)
    quantity = int(input("Enter quantity: "))
    quantity = validateQuantity(quantity)
    print("Product added.\nId: ",id )
    with open("inventory.csv" , "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([id,name,price,quantity])
    
def searchProduct():
    searchId = int(input("Enter id: "))
    with open("inventory.csv", "r") as file:
        reader = csv.reader(file)
        for line in reader:
            if int(line[0]) == searchId:
                print("____________________")
                print("Product name: ",line[1],"\nPrice: ",line[2],"\nQuantity: ",line[3])
                print("____________________")
                break
        else:
                print("Item is not in inventory.")


def updateProduct():
            updateId = int(input("Enter id: "))
            with open("inventory.csv", "r")as file:
                reader = csv.reader(file)
                lines = list(reader)
                found = False
                for i in range(len(lines)):
                    data = lines[i]
                    if int(data[0]) == updateId:
                        newPrice = float(input("Enter new price: "))
                        newPrice = validatePrice(newPrice)
                        
                        newQuantity = int(input("Enter quantity: "))
                        newQuantity = validateQuantity(newQuantity)
                        data[2] = str(newPrice)        
                        data[3] = str(newQuantity)
                        found = True 
                        break   
            if found :
                    with open("inventory.csv", "w", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerows(lines)
                        print("Product updated.")
                                
            else:
                print("Item is not in inventory.")

def sellProduct():    
    sellId = int(input("Enter id: "))
    with open("inventory.csv", "r") as file:
                reader = csv.reader(file)
                found = False
                lines = list(reader)
                for i in range(len(lines)):
                    data= lines[i]
                    if int(data[0]) == sellId:
                        print("Price: ",data[2])
                        print("Quantity available: ",data[3])
                        qSell = int(input("Enter quantity: "))
                        qSell = validateQuantity(qSell)
                        if qSell > int(data[3]):
                            print("Not enough stock")
                        else:
                            amount = float(data[2])*qSell
                            print("Cost: ",amount)
                            data[3] =str(int(data[3])- qSell)
                            found = True
                            break

    if found:
                with open("inventory.csv", "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(lines)
                try:     
                     with open("sale.csv", "r") as file:  
                        reader = csv.reader(file)
                        rows = list(reader)
                        if not rows:
                            pSale = 0
                        else:    
                            pSale = float(rows[0][0])
                except FileNotFoundError:
                    pSale = 0
                totalSale = pSale+amount
                with open("sale.csv", "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([totalSale])   

    else:
                print("Item is not in inventory.")       

def delProduct():
    delId = int(input("Enter id: "))
    found = False
    with open("inventory.csv", "r")as file:
                     reader = csv.reader(file)
                     lines = list(reader)
                     for i in range(len(lines)):
                         data = lines[i]
                         if int(data[0]) == delId:
                             del lines[i]
                             found = True
                             break
    if found:
                     with open("inventory.csv", "w", newline="")as file:
                         writer = csv.writer(file)
                         writer.writerows(lines)
                         print("Product deleted.")
                 
    else:
                     print("Item is not in inventory.")

def displayProducts():
  with open("inventory.csv", "r") as file:
                 reader = csv.reader(file)
                 for data in reader:
                    print("____________________")
                    print("Id: ",data[0])
                    print("Name: ",data[1])
                    print("Price: ",data[2])
                    print("Quantity: ",data[3])
                    print("____________________")

def showTotalValue():
    totalValue = 0
    with open("inventory.csv", "r") as file:
                reader = csv.reader(file)
                for data in reader:
                    totalValue+= float(data[2])*float(data[3])
    print("____________________")            
    print("Total value: ",totalValue)
    print("____________________")            

def displaySale():
    try: 
        with open("sale.csv", "r") as file:
                    reader = csv.reader(file)
                    data = list(reader)
                    if data:
                          sale = float(data[0][0])
                    else: 
                          sale = 0

                    print("____________________")
                    print("Total sale today: ",sale)
                    choice = int(input("Press 0 to reset sale/1 to close window: "))
                    if choice == 0:
                        with open("sale.csv", "w" , newline="") as file:
                            writer = csv.writer(file)
                            writer.writerow([0])
                            print("Sale reset.")  
    except FileNotFoundError:
        print("____________________")
        print("Sale: ", 0)

def displayLowStock():
    count = 0
    with open("inventory.csv", "r") as file:
                reader = csv.reader(file)
                for data in reader:
                        if int(data[3])<10:
                            print("____________________")
                            print(data[1], "left only ", data[3])
                            count += 1

    if count == 0:
                print("______________")
                print("Stock is ok.")        
                                       
while True:
    print("____________________")
    choice = int(input("Choose an option: \n1. Add product\n2. Search product\n3. Update product\n4. Sell product\n5. Delete product\n6. Display all products\n7. Show total inventory value\n8. Display today's sale\n9. Low stock products\n10. Exit\n"))

    match choice:
        case 1:
            addProduct()

        case 2:
            searchProduct()

        case 3:
            updateProduct()

        case 4:
            sellProduct()

        case 5: 
            delProduct()

        case 6:
           displayProducts()
        case 7: 
           showTotalValue()
        case 8:
            displaySale()
        case 9:
            displayLowStock()
        case 10:
            break

        case _:
            print("Invalid input.")



            

