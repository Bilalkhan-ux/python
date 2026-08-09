book = {}
while True:
    choice = input("Choose option: \n1. Add contact\n2. Search contact\n3. Delete contact\n4. Display all contacts\n5. Exit\n")

    match choice:   
            case "1":
                name = input("Enter name: ")
                contact = input("Enter number: ")
                book[name] = contact

            case "2":
                name = input("Enter name: ")
                if name in book:
                     print("Found", book[name])
                else:
                     print("Not found")

            case "3": 
                name = input("Enter name: ")
                if name in book:
                     del book[name]
                     print("Contact deleted")
                else:
                    print("Contact not found")    

            case "4":
                for name , contact  in book.items():
                     print(name ,": ",contact)

            case "5":
              break

            case _:
              print("Invalid input")




