
marks = [65,87,56,78,99]

print(marks)

#List can store different datatypes such as

list = [ 65,76,54,76,'A' , 56.4] 

 #List operations/functions
print(len(marks)) #will print length i.e., 5

print(marks[1])
print(marks[-1]) # to print last index

#to slice a list - list[st:end]

slicedList = marks[0:3]

print(slicedList)

for i in marks:
    print(i)  #to print one by one


# to add value in the end
marks.append(100)
print(marks)

# to add at index
marks.insert(1,88)
print(marks)

#to check if value exist or not
print(67 in marks) # return true of false

# to delete all values
marks.clear()
