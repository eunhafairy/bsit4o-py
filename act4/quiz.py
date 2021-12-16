import random


class Quiz:

    __questions = {
        "Ano ang english ng aso" : ["Horse",
                "Bird",
                "Cow",
                "Dog"],
        "Ano ang english ng kabayo" : ["Dog",
                "Bird",
                "Cow",
                "Horse"],
        "Ano ang english ng pusa" : ["Dog",
                "Chicken",
                "Pig",
                "Cat"],
        "Ano ang english ng puno" : ["Rock",
                "Plant",
                "House",
                "Tree"],
        "Ano ang english ng baso" : ["Monitor",
                "Window",
                "Pencil",
                "Glass"],
        "Ano ang english ng ilaw" : ["Air",
                "Wind",
                "Dark",
                "Light"],
        "Ano ang english ng unan" : ["Bed",
                "Room",
                "Blanket",
                "Pillow"],
        "Ano ang english ng damit" : ["Sock",
                "Handkerchief",
                "Mantle",
                "Clothes"],
        "Ano ang english ng itik" : ["Kitten",
                "Cat",
                "Rabbit",
                "Duck"],
        "Ano ang english ng Baka" : ["Dog",
                "Bird",
                "Horse",
                "Cow"],
        "Ano ang english ng baboy" : ["Cat",
                "Chicken",
                "Dog",
                "Pig"],
        "Ano ang english ng bato" : ["Tree",
                "Plant",
                "House",
                "Rock"],
        "Ano ang english ng lapis" : ["Monitor",
                "Window",
                "Glass",
                "Pencil"],
        "Ano ang english ng hangin" : ["Light",
                "Wind",
                "Dark",
                "Air"],
        "Ano ang english ng kama" : ["Pillow",
                "Room",
                "Blanket",
                "Bed"],
        "Ano ang english ng panyo" : ["Clothes",
                "Sock",
                "Mantle",
                "Handkerchief"],
        "Ano ang english ng bintana" : ["Monitor",
                "Pencil",
                "Glass",
                "Window"],
        "Ano ang english ng dilim" : ["Light",
                "Wind",
                "Air",
                "Dark"],
        "Ano ang english ng kwarto" : ["Pillow",
                "Bed",
                "Blanket",
                "Room"],
        "Ano ang english ng medyas" : ["Clothes",
                "Handkerchief",
                "Mantle",
                "Sock"]
                                

        }

    def __init__(self,  __score = 0, __correctTotal = 0, __incorrectTotal = 0 ) -> None:
        self.__score = __score
        self.__correctTotal = __correctTotal
        self.__incorrectTotal = __incorrectTotal

    def loadQuestions(self,noOfQuestions) ->dict[str,list]:

      
        if(1 <= noOfQuestions <= len(self.__questions)):

                #---------------RANDOMIZE DICT-----------------------
                index = 1
                b = list()
                #store keys to list
                for k in self.__questions.keys():
                        b.append(k)

                #randomize list of keys
                random.shuffle(b)


                #create a new dict using the randomized keys and assign corresponding values.
                c = dict()
                for i in b:
                        c[i] = self.__questions[i]
                        if (index < noOfQuestions):
                                index+=1
                        else:
                                break
                return c
                
        else:
                print("Error. Enter numbers only from 1 -", len(self.__questions))
                return None
               
        
        

    def checkAnswer(self, question_ : str, answer : str) -> bool:

        # isCorrect = False
        # ctr = 1
        # if(list(self.__questions[question_])[3] == answer):
        #         isCorrect = True
        #         self.__correctTotal+=1
        #         self.__score+=50
        #         #correct
        # else:
        #         isCorrect = False
        #         self.__incorrectTotal+=1
        #         #incorrect
        

        # return isCorrect

        isCorrect = False
        correctCtr = 0
        incorrectCtr = 1
        score = 0
        if(list(self.__questions[question_])[3] == answer):
                isCorrect = True
                correctCtr = 1 
                incorrectCtr = 0
                score = 50
        
        self.__correctTotal +=correctCtr
        self.__incorrectTotal+=incorrectCtr
        self.__score+=score
        return isCorrect

   
   #getter 
    #for score
    def getScore(self) -> int:
       return self.__score

    #for correct total
    def getCorrectTotal(self) -> int:
        return self.__correctTotal

    #for incorrect total
    def getIncorrectTotal(self) -> int:
       return self.__incorrectTotal
       #for incorrect total
