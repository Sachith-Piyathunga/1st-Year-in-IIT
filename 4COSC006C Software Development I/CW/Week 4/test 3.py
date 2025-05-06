##names = ["Saman", "Lakshman", 42]
##
##for y in range (1,11): # for loop inside a for loop #basicaly using 2 for loops
##    for x in names:
##        print(y,x)
## 


#While loop

##number = 0 #initilizer
##while (number <10): #conditionn
##    print(number)
##    number = number + 1 #incrementer

##number = 10 
##while (number >0): 
##    print(number)
##    number = number - 1

##number = 1 
##while (number <11): 
##    print(number)
##    number = number + 1



##total = 0
##count = 0
##
##salary = 0.0
##
##while salary >= 0.0 :
##    salary = float(input("Enter your salary : "))
##    if salary >= 0.0:
##        total = total + salary
##        count = count + 1


##fruit = "apple"
##position = 0
##while position < len(fruit):
##    print(fruit[position])
##    position = position + 1


fruit = "apple"
position = 0
while position < len(fruit):
    if(fruit[position] == "e"): #when after the letter l the code  immidiatly stop
        break
    print(fruit[position])
    position = position + 1


fruit = "banana"
for letter in fruit:
    print (letter)


s = "python rocks"
for ch in s:
    print("HELLO")# Hello is printing 12 times cause the"S" ids position in 12 th place
    
