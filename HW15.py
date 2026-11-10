#Name: Oliver Waldrop
#Class: 5th Hour
#Assignment: HW15

import random
#1. Create a for loop with variable i that counts down from 5 to 1 and then prints "Hello World!"
#at the end.
for i in range(5, 0, -1):
    if i == 1:
        print("Hello World!")
    print(i)
#2. Create a for loop that counts up and prints only even numbers between 1 and 30.
for k in range(1, 30 +1):
    if k % 2 == 0:
        print(k)
#3. Create a for loop that prints from 1 to 30 and continues (skips the number) if the number is
#divisible by 3.
for l in range(30):
    l+=1
    if l % 3 == 0:
        continue
    print(l)
#4. Create a for loop that prints 5 different animals from a list.
animals = ["dog", "narwhal", "cat", "chicken", "ROOSTER"]
for animal in animals:
    random.shuffle(animals)
    print(animal)
#5. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")
answer1 = input("Enter a word!???!!!: ")
reverse_answer1 = answer1[::-1]
for o in answer1:
    print(reverse_answer1)
#6. Create a list containing 10 integers of your choice and print the list.
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1)
#7. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers = []
oddNumbers = []
#8. Make a loop that counts the number of even and odd numbers in the list, and prints the
#result after the loop.
for num in list1:
    if num % 2==0:
        evenNumbers.append(num)
    else:
        oddNumbers.append(num)
print(evenNumbers, oddNumbers)


#9. Create a variable that asks the user for an integer and an empty integer variable.
var1 = int(input("Enter a number: "))
var2 = None
#10. Create a loop with a range from 1 to the number the user input. Use the loop to find the
#factorial of that number and print the result. A factorial of a number is that number multiplied
#by every number before it until you reach 1. (For example: 5! is 5 x 4 x 3 x 2 x 1 = 120)
jj = 1
for a in range(1, var1 + 1):
    jj = jj * a
    print(jj)