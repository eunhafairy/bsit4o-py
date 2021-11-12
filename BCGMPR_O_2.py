# #PROBLEM 1
print("\n#PROBLEM 1")
a, b = input("Enter a character and a number respectively, separated by space: ").split()
for num in range(1,int(b)):
    print(a * num)

for num in range(int(b),0, -1):
    print(a * num)

#PROBLEM 2
print("\n#PROBLEM 2")
num = input("Input a number: ")
sum = 0
for a in range((int(num)-1), 0, -1):
    sum+= a**3
print(f"The sum of all cubes is {sum}")   


#PROBLEM 3
print("#PROBLEM 3")
num = input("Input a number: ")
ctr = 1
b = 1
for a in range(1,(int(num)+1)):
    
    if(b < ctr):
       ending = ""
       b+=1
         
    else:
        b = 1
        ctr += 1
        ending = "\n"
    
    print(a, end = ending)


# #PROBLEM 4
print("\n#PROBLEM 4")

sum = 0
ave = 0

while(True):
    a = input("Input a number, press 0 to exit: ")
    if (int(a) == 0):  
        break
    elif((int(a) % 2) != 0):
        sum += int(a)
        ave+=1
   
print(f"The sum of all odd numbers is {sum}.\nThe average of all odd numbers is {sum/ave}.\nThe square root of the sum of all odd numbers is {sum**0.5 : .2f}")


#PROBLEM 5
print("\n#PROBLEM 5")

num = input("Input a number: ")
b = 1
ctr=1
c=0
for a in range(1, (int(num)+1)):
    if(b < ctr):
        b+=1
        
    else:
        b = 1
        ctr += 1
       
            
print(f"The height of the pyramid is {ctr-1}")