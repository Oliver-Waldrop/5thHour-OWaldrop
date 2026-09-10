#Name: Oliver Waldrop
#Class: 5th Hour
#Assignment: HW5

#1. Print Hello World!
print ("Hello World")
#1. Create a list with 5 strings containing 5 different names in it.
list_of_names=["Jake", "Santi", "Anthony", "Wyatt", "Oliver"]
#2. Append a new name onto the Name List.
list_of_names.append(input("Add someone to the list: "))
#3. Print out the 4th name on the list.
print(list_of_names[3])
#4. Create a list with 4 different integers in it.
list_of_numbers=[6, 29, 20, 7, 19]
#5. Insert a new integer into the 2nd spot and print the new list.
list_of_numbers.insert(1, 12)
print(list_of_numbers)
#6. Sort the list from lowest to highest and print the sorted list.
list_of_numbers.sort()
print(list_of_numbers)
#7. Add the 1st three numbers on the sorted list together and print the sum.
sum_numbers= list_of_numbers[0] + list_of_numbers[1] + list_of_numbers[2]
print(sum_numbers)
#8. Create a list with two strings, two variables, and too boolean values.
list_hi = ["bob", "john", 8, 9, False, True]
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print (list_hi[int(input("Give me an index number"))])