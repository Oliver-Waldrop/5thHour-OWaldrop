#Name: Oliver Waldrop
#Class: 5th Hour
#Assignment: HW13

#1. Import the random function
import random
#2. Create a variable called 'temp' that randomly generates a number between 1 and 30
temp = random.randint(1,30)
print (temp)
#3. Go to the link below and convert the code into pseudocode in comments, then code the flowchart completely:
#https://adacomputerscience.org/images/content/computer_science/design_and_development/program_design/figures/ada_cs_design_flow_ifelseif.svg
#If temp is greater or equal to 10
#If temp is greater or equal to 20, print ("It's hot")
#elif temp is greater or equal to 10, print ("It's mild!")
#else, print ("It's mild!")
if temp >= 10:
    if temp >= 20:
        print ("It's hot")
        print ("Thank You")
    elif temp >= 10:
        print ("It's mild!")
        print("Thank You")
else:
    print ("It's cold")
    print("Thank You")
