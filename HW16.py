#Name: Oliver Waldrop
#Class: 5th Hour
#Assignment: HW16


#1. import the "random" library
import random
import math
from operator import truediv

#2. print "Hello World!"
print ("Hello World!")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a = int(input("Enter a whole number: "))
b = int(input("Enter a whole number: "))
c = int(input("Enter a whole number: "))
#4. Add a and b together, then divide the sum by c. Print the result.
sum1 = (a+b) / c
print(sum1)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
print (math.ceil(sum1))
#6. Create a list of five different random integers between 1 and 10.
list1 = [random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10)]
print(list1)
#7. Print the 4th number in the list.
print(list1[3])
#8. Append another integer to the end of the list, also random from 1 to 10.
list1.append(random.randint(1,10))
print(list1)
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
list1.sort()
print(list1)
print(list1[3])
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i =0
while i <=100:
    i+=1
    if i> 100:
        break
    else:
        print(i)
#11. Create a list containing the names of five other students in the classroom.
list2 = ["Santi", "Wyatt", "Jake", "Anthony", "Max"]
#12. Create a for loop that individually prints out the names of each student in the list.
for l in list2:
    print(l)
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
for k in range(0, 100+1):
    k+=1
    if k % 10 == 0:
        break
    else:
        print(k)
#14. Free space. Do something creative. :)
choice1 = int(input("You are trapped in a room. There are 2 doors. To escape, which one do you choose? The red door or the blue door? (1 for red and 2 for blue): "))
if choice1 == 1:
    print("oof... bad choice. You walk in an see the 67 kid. He kills you.")
    print("Game Over pal")
else:
    print("Nice choice!")
choice2= int(input("You then walk through the blue door and see 2 new doors. They are the same color. Which one do you choose now?: "))
if choice2 == 1:
    print("Wow good thinking!")
else:
    print("Well good luck with that... You walk in and then see your mom. You forgot to do the dishes... She throws a sledgehammer at you.")
    print("Game Over...")
choice3= int(input("You walk through the red door. Now there are 3 doors. All of them are red. They are all already open. Which one do you choose?: "))
if choice3 == 2:
    print("Oof... that was a horrid choice. You walk into it and see chucky cheese. You never liked his pizza. You die of starvation")
elif choice3 == 1:
        print("Ooh I see you! You walk in and then you see your dog! He is dancing.")
else:
    print ("You got skinned alive. Oh well")
    print("Game Over...")
choice4= int(input("Do you join your dog in dancing? (1 for yes 2 for no): "))
if choice4 == 1:
    print("Just kidding you never had a dog. He turns into a giraffe and takes out a chainsaw. You get sawwed to death.")
    print("Game Over?")
else:
    print("You die because your dog has a gun. Oh well")
    print("Game Over")
if choice4 == 1:
    print("You hear rumbling...")
    print("Then Chuck Norris comes out of nowhere and kills the giraffe!")
    print("You survive! Good job!")
else:
    print("You won the game!")