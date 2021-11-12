# #PROBLEM 1
number_list = [
        ["  #", "  #", "  #", "  #", "  #"], #1
        ["###", "  #", "###", "#  ", "###"], #2
        ["###", "  #", "###", '  #',"###"], #3
        ["# #", "# #", "###", "  #", "  #"], #4
        ["###", "# ", "###", "  #", "###"], #5
        ["###", "#  ", "###", "# #", "###"], #6
        ["###", "  #", "  #", "  #", "  #"], #7
        ["###", "# #", "###", "# #", "###"], #8
        ["###","# #", "###", "  #","###"], #9
        ["###", "# #", "# #", "# #", "###"] #0
    
]

while True:
    user_input = input("Enter a number: ")
    if user_input.isnumeric():
        break
    else:
        print("Invalid input")

numbers = []
for i in str(user_input):
    numbers.append(number_list[(int(i)-1)])

for i in range(5):
    for x in numbers:
        print(x[i], end=" ")
    print()

#PROBLEM 2


alphabet_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

while True:
    user_input = input("Please select [0]Cipher/[1]Decipher: ")
    if user_input.isnumeric() and (user_input == '0' or user_input == '1'):
        _type = user_input
        break
    else:
        print("Invalid input.", end = " ")

while True:
    user_input = input("Enter the number of shift (1-25): ")
    if user_input.isnumeric() and (int(user_input) >= 1 and  int(user_input) <= 25):
        _shift = int(user_input)
        break
    else:
        print("Invalid shift.", end = " ")

user_input = input("Enter the message: ")

if int(_type) == 0:
    for char in user_input:
        if not char.isalpha():
            print(char, end="")
        else:
            _try = "".join(alphabet_list)
            ctr = _try.index(char.upper())
            print(alphabet_list[ctr+_shift], end="")
       
else:
    for char in user_input:
        if not char.isalpha():
            print(char, end="")
        else:
            _try = "".join(alphabet_list)
            ctr = _try.index(char.upper())
            print(alphabet_list[ctr-_shift], end="")

# PROBLEM 3
#solution 1
user_input = input("Solution 1: Enter Word/s: ")
user_input = user_input.replace(" ", "")
user_input = user_input.lower()
reversed_user_input = ""

if user_input == "":
    print("It's not a palindrome")
else:
    for num in range((len(user_input)-1), -1, -1):
        reversed_user_input+=user_input[num]

    if user_input == reversed_user_input:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")

#PROBLEM 4

user_input = input("Enter First string: ")
user_input2 = input("Enter Second string: ")

user_input = user_input.replace(" ", "")
user_input = user_input.lower()
user_input2 = user_input2.replace(" ", "")
user_input2 = user_input2.lower()

user_input = "".join(sorted(user_input))
user_input2 = "".join(sorted(user_input2))

if user_input == user_input2:
    print("Anagrams")
else:
    print("Not anagrams")


#PROBLEM 5

while True:
    user_input = input("Enter your bday: ")
    if user_input.isnumeric() and len(user_input) == 8:
        break
    else:
        print("Invalid input. ", end = " ")

while True:
    sum = 0
    for char in user_input:
        sum+=int(char)
        
    if len(str(sum)) == 1:
        break
    user_input=str(sum)
    
print(sum)