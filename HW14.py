#Name: Oliver Waldrop
#Class: 5th Hour
#Assignment: HW14
import random
import time
from operator import truediv

#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
i=5
while i >=1:
    print(i)
    i-=1
else:
    print("Hello World!")
#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
j = 30
while j>=1:
    j-=1
    if j%2==0:
        print(j)

else:
    print()
#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.
k=1
while k<30:
    k+=1
    if k%3==0:
        continue
    print(k)
#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
l = random.randint(1,6)
while l:
    l=random.randint(1,6)
    print(l)
    if l == 1:
        break
#5. Create a while loop that asks for a number input until the user inputs the number 0.
while True:
    if input("Enter a number 0 - 10: ") == "0":
        print("correcto!")
        break
    elif input("Enter a number 0 - 10: ") !=  "0":
        print("incorrecto!")