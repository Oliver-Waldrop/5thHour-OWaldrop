#Name: Oliver Waldrop
#Class: 5th Hour
#Assignment: HW9

#1. Print Hello World!
print ("Hello World!")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
Super_Cool_Dictionary = {
    "num1" : 5,
    "num2" : "George",
    "num3" : [5, 3, 975432211122]
}
#3. Print the keys of the dictionary from #2.
print (Super_Cool_Dictionary)
#4. Print the values of the dictionary from #2
print (Super_Cool_Dictionary.values())
#5. Print one of the three numbers from the list by itself
print (Super_Cool_Dictionary["num3"][1])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
Super_Cool_Dictionary.update ({"num4" : 9})
#7. Print the entire dictionary from #2 with the updated key and value.
print (Super_Cool_Dictionary)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
Dict2 = {"Student1" : {
         "Name" : "Wyatt",
         "Grade" : "9",
         "Height" : "8'10"
},
"Student2" : {
         "Name" : "Santi",
         "Grade" : "9",
         "Height" : "3'9"
},
"Student3" : {
         "Name" : "Anthony",
         "Grade" : "9",
         "Height" : "4'7"
},
}
#9. Print the names of all three classmates on the same line.
print(Dict2["Student1"]["Name"],Dict2["Student2"]["Name"],Dict2["Student3"]["Name"])
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
Dict2.pop("Student3")
print(Dict2)