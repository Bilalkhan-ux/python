# range(start , end , step)

# while loop

counter = 0

while counter <= 5:
    print(counter * "X") # string multiplies with int
    counter+= 1

#for loop

num = range(5)
for i in num:
    print(i)

for i in range( 1, 6 ):
    print(i*2)

# even numbs

for i in range(2, 21, 2):
    print(i, end = " ") # print starts from new line. end = " " start it from same line

# Practice exercise

for i in range(1,21,3):
    print(i, end = " ")

print(" ")

for i in range(57 , 571, 57):
    print(i, end = " " ) 

for i in range(3,50, 3):
    if i == 15:
        continue
    print(i,end = " ")    

a = int(input("Enter a: "))
b = int(input("Enter b: "))

for i in range(1, 1001):
    if i%a == 0 and i % b == 0:
        print (i)
        break
    else:
        print("No common multiple")