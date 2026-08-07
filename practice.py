# Question: give a list of following roll no , print all unique roll nos
rollNumbers = {101, 105,102,101,108,105,110}
print(rollNumbers)

#Another question
emp = [ ( 101, "Alice" , 50000) , (102 , "King" , "80000") , (103 , "Bob" , "60000")]

id = int(input("Enter id: "))

for i in emp:
    if i[0] == id:
        print("Found")
        print(i)
        break

else:
    print("Not found")

