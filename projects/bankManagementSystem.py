import csv
def loadFile():
    with open("accounts.csv", "r") as file:
            reader = csv.reader(file)
            return list(reader)
def saveFile(data):
    with open("transactions.csv", "a", newline="") as file:
        writer =  csv.writer(file)
        writer.writerow(data)
def saveAccounts(lines):
    with open("accounts.csv", "w", newline="") as file:
        writer =  csv.writer(file)
        writer.writerows(lines)

def validateAmount():
    amount = int(input("Enter amount: "))
    while amount <= 0:
        amount = int(input("Amount should be greater than 0 "))
    return amount

def validatePin(data):
    pin = int(input("Enter pin: "))
    while int(data[2]) != pin:
        pin = int(input("Wrong pin! Enter pin again: "))

    return pin

def validateId():
    while True:
        try:
            id = int(input("Enter id: "))
            break
        except ValueError:
            print("Invalid input.")

    return id

def createAccount():
    id = 1
    try :
        with open("accounts.csv", "r") as file:
            reader = csv.reader(file)
            for data in reader:
                if data[0]>=str(id):
                    id = int(data[0])+1
    except FileNotFoundError:
        id = 1
    name = input("Enter your name: ")
    pin = int(input("Enter pin: "))
    with open("accounts.csv", "a",newline="")as file:
        writer = csv.writer(file)
        writer.writerow([id,name,pin,0])
        print("Account created.")
        print("Your id is: ",id)
        print("***************")

def deposit():
    id = validateId()
    lines = loadFile()
    for i in range(len(lines)):
            if int(lines[i][0]) == id:
                validatePin(lines[i])
                amount = validateAmount()
                lines[i][3] =int(lines[i][3])+ amount 
                saveAccounts(lines)
                print("Amount deposited.")
                print("***************")
                saveFile([id,"Deposited: ",amount])
                break
    else:
        print("Account doesn't exist.")

def withdraw():
    id = validateId()
    lines = loadFile()
    for i in range(len(lines)):
        if int(lines[i][0]) == id:
            validatePin(lines[i])   
            amount = validateAmount()
            if amount > int(lines[i][3]):
                print("Not enough balance.")
            else:
                lines[i][3] =int(lines[i][3]) - amount
                saveAccounts(lines)
                print("Amount withdrawn.")
                print("***************")                
                saveFile([id,"Withdraw: ",amount])
                break
    else:
        print("Account doesn't exist.")

def checkBalance():                
    id = validateId()
    lines = loadFile()
    for data in lines:
            if int(data[0]) == id:
                validatePin(data) 
                print("Balance: ",data[3])
                print("***************")
                break
    else:
        print("Account doesn't exist")    

def transferMoney():
    found = False
    id = validateId()
    lines = loadFile()
    for i in range(len(lines)):
            if int(lines[i][0]) == id:
                validatePin(lines[i]) 
                transferId = int(input("Enter id of tranfer account: "))
                for j in range(len(lines)):
                    if int(lines[j][0]) == transferId:
                        amount = validateAmount()
                        if amount > int(lines[i][3]):
                            print("Not enough balance.")
                        else:
                            lines[i][3] =int(lines[i][3]) -  amount
                            lines[j][3]=int(lines[j][3]) + amount
                            saveFile([id,"Transferred: ",amount, " to ", lines[j][1]])
                            saveFile([transferId," Received: ",amount, " from ", lines[i][1]])
                            saveAccounts(lines)
                            print("Amount tranferred.")
                            print("***************")
                            found = True
                                
                            break
    if found == False:  
        print("Account doesn't exist")
        
def delAccount():
    found = False
    id = validateId()
    lines = loadFile()
    for i in range(len(lines)):
        if int(lines[i][0]) == id:
            validatePin(lines[i]) 
            del lines[i]
            found = True
            break
    if found:        
        saveAccounts(lines)
        print("account deleted.")  
        print("***************")
    else:
        print("Account doesn't exist.")


def display():
        lines = loadFile()
        for data in lines:   
            print("Id: ",data[0]) 
            print("Name: ",data[1]) 
            print("Balance: ",data[3]) 
            print("****************")
            
def transactions():
    found = False
    id = validateId()
    lines = loadFile()
    for i in range(len(lines)):
            if int(lines[i][0]) == id:
                found =True
                validatePin(lines[i])               
                try:
                    with open("transactions.csv", "r", newline="") as file:
                        reader = csv.reader(file)
                        lines = list(reader)
                        for data in lines:
                            if data[0] == str(id):
                                print(data)
                except FileNotFoundError:
                    print("No transactions found.")
                break
    if not found:
        print("account doesn't exist.")                        
while True :
    choice = int(input("1. Create account\n2. Deposit money\n3. Withdraw money\n4. Check balance\n5. Transfer money\n6. Transaction history\n7. Delete account\n8. Display account\n9. Exit\n"))

    match choice:
        case 1:
            createAccount()
        case 2:
            deposit()
        case 3:
            withdraw()                    
        case 4:
            checkBalance()
        case 5:
            transferMoney()    
        case 6:
            transactions()
        case 7:
            delAccount()
        case 8:
            display()
        case 9:
            break
        case _:
            print("Invalid input")