from quiz import Quiz as q

while(True):
    print("\n====WELCOME TO TAGALOG-ENGLISH QUIZ GAME====\n")
    newQuiz = q()
    #check if entered number is numeric and if it is within the scope
    while(True):
        try:
            noOfQuestion = int(input("Enter the number of questions: "))
        except:
            print("Enter only numeric number")
            continue
        
    
        if (newQuiz.loadQuestions(noOfQuestion) != None):
            break
     
        

    #load questions
    qNo = 1
    myDict = newQuiz.loadQuestions(noOfQuestion)
    for k,v in myDict.items():

        print(f"Question {qNo}: " + k + '?')
        letterList = ["[A] ","[B] ","[C] ","[D] " ]
        itr = 0
        answerList = list()

        for choice in list(v):
            print(letterList[itr], choice)
            itr+=1
            answerList.append(choice)
        
        #check eligibility of input
        while(True):
            try:
                yourAnswer = str(input("Enter your answer (letter only): "))
            except:
                print("Error. Please enter only characters a,b,c and d.")
                continue

            if (yourAnswer == 'A' or yourAnswer == 'a') :
                ctr = answerList[0]
                break
            elif (yourAnswer == 'B' or yourAnswer == 'b'):
                ctr = answerList[1]
                break
            elif (yourAnswer == 'C' or yourAnswer == 'c'):
                ctr = answerList[2]
                break
            elif (yourAnswer == 'D' or yourAnswer == 'd'):
                ctr = answerList[3]
                break
            else:
                print("Error. Please enter only characters a,b,c and d.")

            
        #check if correct

        if(newQuiz.checkAnswer(k, ctr)):
            print("Hooray! You got 50 points!")
        else:
            print("Oops! No points this time.")
        print("• User Current Score:", newQuiz.getScore(),"•")
        qNo+=1
        print("=============================")

    print("|        SCORE BOARD        |")
    print("=============================")
    print("Total Score:", newQuiz.getScore())
    print("Total Correct:", newQuiz.getCorrectTotal())
    print("Total Incorrect:", newQuiz.getIncorrectTotal())

    while (True):
        try: 
            playAgain = str(input("\nDo you want to play again? Enter Yes or No: "))
        except:
            print("Please enter only string characters.")
            continue
        playAgain = playAgain.lower()
        playAgain = playAgain.strip()
        if(playAgain == "yes" or playAgain == "no"):
            break
        else:
            print("Please enter only Yes or No.")

    if(playAgain == 'yes'):
        continue
    else:
        print("Thank you for playing!")
        break