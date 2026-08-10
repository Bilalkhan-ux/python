def verifyAccount(bank, id):
    if id in bank:
        pin = int(input("Enter your pin: "))
        if pin == bank[id][1]:
            return True
        else:
            print("Wrong pin")
    else:
        print("Account doesn't exist")
        return False

bank = {}
transactions = {}
i = 10000
while True:
    choice = input("Choose option\n1. Create account\n2. Deposit\n3. Withdraw\n4. check balance\n5. Transfer money\n6. Display account\n7. Exit\n")

    match choice:
        case "1":
            name = input("Enter name: ")
            pin = int(input("Enter pin: "))
            id = i
            i+=1
            balance = 0
            bank[id]= [name,pin, balance]
            print("Account created\nYour id is ",id)
            transactions[id]= []

        case "2":
            userId = int(input("Enter your id: "))
            if (verifyAccount(bank, userId)):
                    amount = int(input("Enter amount to deposit: "))
                    if amount <= 0:
                        print("You can't enter negative amount")
                    else:
                        bank[userId][-1] += amount
                        print("Deposited")
                        transactions[userId].append({"Deposited": amount})
           

        case "3":
            userId = int(input("Enter your id: "))
            if (verifyAccount(bank, userId)):
                    amount = int(input("Enter amount to withdraw: "))
                    if amount <= 0:
                        print("You can't enter negative amount")
                    else:    
                        if amount > bank[userId][-1]:
                            print("Not enough balance")
                        else: 
                            bank[userId][-1]-=amount 
                            print("Money withdrawn")
                            transactions[userId].append({"Withdrawn ": amount})

        case "4":
            userId = int(input("Enter your id: "))
            if (verifyAccount(bank, userId)):
                    print("Balance: ", bank[userId][-1])
                    

        case "5":
            userId = int(input("Enter your id: "))
            if (verifyAccount(bank, userId)):
                    transferAccount = int(input("Enter id of account you want to tranfer money to: "))
                    if transferAccount in bank:
                        if userId == transferAccount:
                            print("Can't transfer to yourself.")
                        else:
                            amount = int(input("Enter amount to transfer: "))
                            if amount <= 0:
                                print("You can't enter negative amount.")
                            else:
                                if amount > bank[userId][-1]:
                                    print("Not enough balance")
                                else: 
                                    bank[userId][-1]-=amount
                                    bank[transferAccount][-1]+=amount
                                    print("Transferred successfully")
                                    transactions[userId].append({"Transferred to":bank[transferAccount][0] ,"Amount ": amount })
                                    transactions[transferAccount].append({"Received from":bank[userId][0] ,"Amount ": amount })
                    else:
                        print("Account doesn't exist")
                  

        case "6":
            userId = int(input("Enter id: "))
            if (verifyAccount(bank, userId)):
                print("Name: ", bank[userId][0], "\nBalance: ", bank[userId][-1])
                print("Transactions: ")
                for history in transactions[userId]:
                    print (history)
           
        case "7":
            break

        case _:
            print("Invalid input")
                           




