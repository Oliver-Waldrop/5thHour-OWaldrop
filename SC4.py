#Name: Oliver Waldrop
#Class: 5th Hour
#Assignment: SC4

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.
num_of_players = int(input("How much players are there?: "))
score = 0
for player in range(1, num_of_players + 1):
    rating = int(input(f"Judge {player}, rate the model 1-5: "))
    score+=rating
    while rating > 5 or rating < 1:
        print("Put in a number between 1 and 5")
        rating = int(input(f"Judge {player}, rate the model 1-5: "))
average_score = score/num_of_players
print(average_score)