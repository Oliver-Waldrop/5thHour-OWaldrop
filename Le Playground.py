Game_characters = {
    1: {
    "Name" : "John-a-tron",
    "Health" : 100,
    "Hunger" : 100,
    "Energy" : 100,
},
    2 : {
    "Name" : "Jessica",
    "Health" : 100,
    "Hunger" : 100,
    "Energy" : 100,
},
    3 : {
    "Name" : "James",
    "Health" : 100,
    "Hunger" : 100,
    "Energy" : 100,
},
    }
print("Welcome to the Game!")
print("Press 1 for John-a-tron")
print("Press 2 for Jessica")
print("Press 3 for James")
choice1 = int(input("Who do you want to be?: "))
if choice1 == 1:
    chosen= Game_characters[1]
elif choice1 == 2:
    chosen= Game_characters[2]
elif choice1 == 3:
    chosen= Game_characters[3]
else:
    print("Not a valid choice!")
    chosen = None
if choice1 == 1:
        print("You are now John-a-tron")
elif choice1 == 2:
        print("You are now Jessica")
else:
        print("You are now James")
print("")
print("Welcome to the Game!")
print("Answer 1 or 2")
print("")
print(Game_characters[choice1]["Name"])
print(f"Health : {chosen['Health']}")
print(f"Energy : {chosen['Energy']}")
Game_characters[1].update({"Hunger": 60})
print(f"Hunger : {Game_characters[1]['Hunger']}")
print("")
c2 = int(input("You are now in your apartment. You haven't eaten today. Should you get food, or will you go for a walk?: "))

if c2 == 1:
    print("You are now in a shop.")
else:
    print("You are out for a walk")

if c2 == 1:
    int(input("Do you want to eat a bagel or a breakfast sandwich?: "))
else:
    int(input("You find a dog. Do you adopt it?: "))