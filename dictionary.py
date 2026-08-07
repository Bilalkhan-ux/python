# Dictionary - key => value pairs

marks = {"Eng": 89, "Math": 78 , "Science": 87}
print(marks["Eng"]) # to print specific value

#to modify value

marks["Math"] = 81

print(marks["Math"]) #81

for i in marks:
    print(i , marks[i])