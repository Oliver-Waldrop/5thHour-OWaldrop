#Name: Oliver Waldrop
#Class: 5th Hour
#Assignment: HW8


#1. Import the "random" library
import random
#2. print "Hello World!"
print ("Hello World!")
#3. Create three different variables that each randomly generate an integer between 1 and 10
roll1 = random.randint(1,10)
roll2 = random.randint(1,10)
roll3 = random.randint(1,10)
#4. Print the three variables from #3 on the same line.
print (roll1, roll2, roll3)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
sum1 = roll1 + 2
sum2 = roll2 - 4
sum3 = roll3 * 1.5
#6. Print each result from #5 on the same line.
print (sum1, sum2, sum3)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
list1 = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
#8. Sort the list in #7 and print it.
list1.sort()
print (list1)
#9. Add together the highest three numbers in the list from #7 and print the result.
sum4 = list1[1] + list1[2] + list1[3]
print (sum4)
#10. Create a list with 5 names of other students in this class and print the list.
list2 = ["Santi", "Wyatt", "Jake", "Anthony", "Cruz"]
print (list2)
#11. Shuffle the list in #10 and print the list again.
random.shuffle(list2)
print (list2)
#12. Print a random choice from the list of names from #10.
print (random.choice(list2))