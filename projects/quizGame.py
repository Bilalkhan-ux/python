import random

def questions(qs):
    score = 0
    questionsList = [
        ("What is the capital of pakistan\nA. Lahore\nB. Karachi\nC. Islamabad\nD. Peshawar\n" , 'C'),
        ("Which language is mainly used for AI and Machine Learning?\nA. Python\nB. HTML\nC. CSS\nD. SQL\n", 'A'),
        ("What is 5 x 6?\nA) 20\nB) 25\nC) 30\nD) 35\n", 'C'),
        ("Which planet is known as the Red Planet?\nA) Earth\nB) Mars\nC) Jupiter\nD) Venus\n", 'B'),
        ("Which keyword is used to define a function in Python?\nA) function\nB) define\nC) def\nD) fun\n", 'C') ]

    random.shuffle(questionsList)

    for q , a in questionsList[:qs]:
        ans = input(q).upper()
        if ans == a:
            score+=1
            print("Correct")
        else: 
            print("Oops\nCorrect answer is: ", a)    

    return score

qs = int(input("How many questions quiz you want to take(Total: 5): "))
while True:
    if  5 >= qs >= 1:
        score = questions(qs)
        print("Score: ",score,"/",qs)
        print("Percentage: ", (score/qs)*100, "%")
        break
    else:
        qs = int(input("Please enter a number between 1 and 5: "))



    
    