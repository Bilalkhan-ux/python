def numStat():
    total=0
    avg = 0
    largest = float('-inf')
    smallest = float('inf')
    evenList = []
    oddList = []
    numbers = []
    count = 0
    num = int(input("Enter number: "))
    while num != 0:
        count+=1
        total+=num

        if num > largest:
            largest = num

        if num<smallest:
            smallest = num

        if num%2 == 0:
            evenList.append(num)
        else:
            oddList.append(num)

        numbers.append(num)
        num = int(input("Enter number: "))

    uniqueNum = set(numbers)
    print("Total: ",total)
    print("Average: ", total/count)
    print("Largest: ", largest)
    print("Smallest: ", smallest)
    print("Even: ", evenList)
    print("Odd: ", oddList)
    print("Unique: ", uniqueNum)

numStat()

