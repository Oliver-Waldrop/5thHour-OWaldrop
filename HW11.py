#Name: Oliver Waldrop
#Class: 5th Hour
#Assignment: HW11
import random

#1. Print "Hello World!"
print ("Hello World!")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
list1 = [random.randint (1,100), random.randint (1,100), random.randint (1,100)]

#3. Print the list.
print (list1)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if list1[0] >= list1[1] and list1[0] >= list1[2]:
    print (f"{list1[0]} is the highest number")
    num = list1[0]
elif list1[1] >= list1[0] and list1[1] >= list1[2]:
    print (f"{list1[1]} is the highest number")
    num = list1[1]
elif list1[2] >= list1[0] and list1[2] >= list1[1]:
    print (f"{list1[2]} is the highest number")
    num = list1[2]
#5. Tie the result (the largest number) from #4 to a variable called "num".
print (num)
#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 2 == 0:
    if num % 3 == 0:
        print ("divisible by both")
    else:
        print("divisible by 2")
else:
    if num % 3 == 0:
        print ("divisible by 3")
    else:
        print ("divisible by neither")
