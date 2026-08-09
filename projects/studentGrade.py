def avg (marks):
    total = 0
    for i in marks:
        total+=i

    l = len(marks)
    return total/l

def gradeCalc(avgMarks):
    if avgMarks>80:
        return 'A'
    elif avgMarks >60 and avgMarks<=80:
        return 'B'
    elif avgMarks >40 and avgMarks <=60:
        return 'C'
    else:
        return 'F'

def highestMarks(avgMarks):
    maxMarks = avgMarks[0]
    for i in avgMarks:
        if i > maxMarks:
            maxMarks = i
    return maxMarks

students = {"Bilal": [87,65,99] , "Ali":[76,87,65], "Khan":[71,76,85],"Mustafa":[86,64,86]}

avgMarks = []
for i in students:
    average = avg(students[i])
    avgMarks.append(average)

j = 0
for i in students:
    print("Name: ",i)
    print("Average marks: ",avgMarks[j])
    grade = gradeCalc(avgMarks[j])
    print("Grade: ",grade)
    j+=1
    print(" ")

print("Highest marks: ", highestMarks(avgMarks))



