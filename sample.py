import random


question = {
                        "Q1" : ["A. Q1 Answer 1",
                                "B. Q1 Answer 2",
                                "C. Q1 Answer 3",
                                "D. Q1 Answer 4"],
                        "Q2" : ["A. Q2 Answer 1",
                                "B. Q2 Answer 2",
                                "C. Q2 Answer 3",
                                "D. Q2 Answer 4"],
                        "Q3" : ["A. Answer 1",
                                "B. Answer 2",
                                "C. Answer 3",
                                "D. Answer 4"],
                        "Q4" : ["A. Answer 1",
                                "B. Answer 2",
                                "C. Answer 3",
                                "D. Answer 4"],
                        "Q5" : ["A. Answer 1",
                                "B. Answer 2",
                                "C. Answer 3",
                                "D. Answer 4"],
                        "Q6" : ["A. Answer 1",
                                "B. Answer 2",
                                "C. Answer 3",
                                "D. Answer 4"],
                        "Q7" : ["A. Answer 1",
                                "B. Answer 2",
                                "C. Answer 3",
                                "D. Answer 4"],
                        "Q8" : ["A. Answer 1",
                                "B. Answer 2",
                                "C. Answer 3",
                                "D. Answer 4"],
                        "Q9" : ["A. Answer 1",
                                "B. Answer 2",
                                "C. Answer 3",
                                "D. Answer 4"],
                        "Q10" : ["A. Answer 1",
                                "B. Answer 2",
                                "C. Answer 3",
                                "D. Answer 4"],
                        "Q11" : ["A. Answer 1",
                                "B. Answer 2",
                                "C. Answer 3",
                                "D. Answer 4"],
                        "Q12" : ["A. Answer 1",
                                "B. Answer 2",
                                "C. Answer 3",
                                "D. Answer 4"],
                        "Q13" : ["A. Answer 1",
                                "B. Answer 2",
                                "C. Answer 3",
                                "D. Answer 4"],
                        "Q14" : ["A. Answer 1",
                                "B. Answer 2",
                                "C. Answer 3",
                                "D. Answer 4"],
                        "Q15" : ["A. Answer 1",
                                "B. Answer 2",
                                "C. Answer 3",
                                "D. Answer 4"],
                        "Q16" : ["A. Answer 1",
                                "B. Answer 2",
                                "C. Answer 3",
                                "D. Answer 4"],
                        "Q17" : ["A. Answer 1",
                                "B. Answer 2",
                                "C. Answer 3",
                                "D. Answer 4"],
                        "Q18" : ["A. Answer 1",
                                "B. Answer 2",
                                "C. Answer 3",
                                "D. Answer 4"],
                        "Q19" : ["A. Answer 1",
                                "B. Answer 2",
                                "C. Answer 3",
                                "D. Answer 4"],
                        "Q20" : ["A. Answer 1",
                                "B. Answer 2",
                                "C. Answer 3",
                                "D. Answer 4"],
                        

    }



def loadQuestions(noOfQuestions : int) -> dict[str,list]:
        
        #---------------RANDOMIZE DICT-----------------------
        index = 1
        b = list()
        #store keys to list
        for k in question.keys():
            b.append(k)

        #randomize list of keys
        random.shuffle(b)


        #create a new dict using the randomized keys and assign corresponding values.
        c = dict()
        for i in b:
            c[i] = question[i]
            if (index < noOfQuestions):
                index+=1
            else:
                break
        return c

print(loadQuestions(2))