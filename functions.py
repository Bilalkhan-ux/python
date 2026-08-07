from math import sqrt

def calcGST(price):
    return (price + price*0.18)


price = float(input("Enter price: "))
gstPrice = calcGST(price)
print (gstPrice)

print(sqrt(16))


def check(num):
    if num%2 == 0:
        print("Even")
    else:
        print("Odd")

num = int(input("Enter a number: "))
check(num)

# Vowel counter
def counter (str):
    count = 0
    str = str.lower()
    for i in str:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            count+=1

    print(count)

str = "My name is Bilal Khan"
counter(str)

# prime checker

def prime(num):
    if num < 2:
        print("Not prime")
    else:
        for i in range(2, num):
            if num % i == 0:
                print("Not prime")
                break

        else:
            print("Prime")

num = int(input("Enter number: "))
prime(num)



# average of marks calculator

def average(marks):
    sum = 0
    for i in marks:
        sum += i

    length = len(marks)

    return sum/length

marks = [76,45,87,65,67,99]
avg = float(average(marks))
print("Average: ", avg) 
