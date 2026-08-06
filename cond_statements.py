
marks = 76

if marks > 80:
    print("Grade A")
elif marks > 60 and marks<80:
    print("Grade B")
else:
    print("Fail")    

#mini project

a = int(input("Enter number: "))
b = int(input("Enter number 2: "))
oper = input("Enter operator (+ , - , * , / , % , **): ")

if oper == "+" :
    print(a+b)
elif oper == "-":
    print(a-b)    
elif oper == "*":
    print(a*b)
elif oper == "/":
    print(a/b)
elif oper == "%":
    print(a%b)  
elif oper == "**":
    print(a**b)      
else:
    print("Invalid input")    