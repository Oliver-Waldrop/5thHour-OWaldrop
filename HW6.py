#Name: Oliver Waldrop
#Class: 5th Hour
#Assignment: HW6


#1. Create a list with 9 different numbers inside.
list_1 = [1, 2, 3, 4, 5, 7, 8, 8.5, 9]
#2. Sort the list from highest to lowest.
list_1.sort(reverse=True)
print(list_1)
#3. Create an empty list.
list_2 = []
#4. Remove the median number from the first list and add it to the second list.
list_1.pop(4)
list_2.insert(0, 5)
#5. Remove the first number from the first list and add it to the second list.
list_1.pop(0)
list_2.insert(1,9)
#6. Print both lists.
print(list_1)
print(list_2)
#7. Add the two numbers in the second list together and print the result.
sum_1 = sum(list_2)
print(sum_1)
#8. Move the number back to the first list (like you did in #4 and #5 but reversed).
list_2.pop(0)
list_1.append(14)
#9. Sort the first list from lowest to highest and print it.
list_1.sort()
print(list_1)