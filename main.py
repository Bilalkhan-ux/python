print ("Hello")
age = 21
print("My name is Bilal and my age is " , age)


age = input("Enter age: ")  
print("Age: ",age, type(age))
#anything type of data we take input will be stored as "str"

age = int(age) # type casting
print(age, type(age))

num = 255
print(num+2.5) #type conversion

#sum program

a = int(input("Enter a: "))
b = int(input("Enter b: "))
sum = a+b
print("Total: ", sum)