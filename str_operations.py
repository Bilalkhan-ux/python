#string operations

name = "Mr President"

print(name.upper())  #it doesn't change the original str permanently
print(name.lower())
print (name)

#to find the letters in word. It returns index 

print(name.find("ent")) #it will return index 9 .
print(name.find("snt")) # returns -1 if letters doesn't exist

#replace

print(name.replace("President" , "Prince"))
 #will print Mr Prince, doesn't permanently change str

#check presence

print("P" in name) # return true or false

# Practice exercise

price1= float(input("Enter price 1: "))
price2= float(input("Enter price 2: "))
price3= float(input("Enter price 3: "))
total = price1+price2+price3
print("Total: ", total)
print("Average price: " , total/3)

sName = input("Enter superhero name: ")
print("S" in sName.upper())

