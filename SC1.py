#Name: Oliver Waldrop
#Class: 5th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game.
Game_Creatures = {
    "Creature_1" : {
    "Name" : "Dragosaur",
    "Damage" : 45,
    "Health" : 180,
},
    "Creature_2" : {
"Name" : "Avocadoraptor",
    "Damage" : 22,
    "Health" :130,
},
"Creature_3" : {
    "Name" : "John-O-Copter",
    "Damage" : 40,
    "Health" : 200,
},
"Creature_4" : {
    "Name" : "George Cooper",
    "Damage" : 55,
    "Health" : 250,
},
"Creature_5" : {
    "Name" : "Brisket",
    "Damage" : 15,
    "Health" : 90,
    },
}
dmg1 = int(input("How much damage would you like to change to Dragosaur? : "))
Game_Creatures["Creature_1"]["Damage"] = dmg1
print(Game_Creatures["Creature_1"])

dmg1 = int(input("How much damage would you like to change to Avocadoraptor? : "))
Game_Creatures["Creature_2"]["Damage"] = dmg1
print(Game_Creatures["Creature_2"])

dmg1 = int(input("How much damage would you like to change to John-O-Copter? : "))
Game_Creatures["Creature_3"]["Damage"] = dmg1
print(Game_Creatures["Creature_3"])

dmg1 = int(input("How much damage would you like to change to George Cooper? : "))
Game_Creatures["Creature_4"]["Damage"] = dmg1
print(Game_Creatures["Creature_4"])

dmg1 = int(input("How much damage would you like to change to Brisket? : "))
Game_Creatures["Creature_5"]["Damage"] = dmg1
print(Game_Creatures["Creature_5"])