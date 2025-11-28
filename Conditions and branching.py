# Conditions and branching
"""Player Name	Sport	Achievements
Serena Williams	Tennis	23 Grand Slams
Lionel Messi	Soccer	7 Ballon d'Ors
Michael Phelps	Swimming	23 Gold Medals
Usain Bolt	Athletics	8 Gold Medals
Roger Federer	Tennis	20 Grand Slams
Cristiano Ronaldo	Soccer	5 Ballon d'Ors"""

# Quiz: 1 Write a Python program to check if a player Lionel Messi has more than 10 achievements.
# If the condition is true, print the player's name, sport, and achievements else print does not have more than 10 achievements.
player1 = "Lionel Messi"
achievements = 7
sport = "soccer"
if(player1 == "Lionel Messi") and (achievements > 10):
    print(player1, sport, achievements)
else: 
    print(player1,"does not have more than 10 achievements")

# Or like this:
if achievements > 10:
    print(f"{player1} plays {sport} and has {achievements} achievements.")
else:
    print(f"{playe1} does not have more than 10 achievements.")

# Quiz 2: Write a Python program to check if a player belongs to the sport Tennis 
# or has exactly 20 achievements. If the condition is true, print a success message.

player1 = "Roger Federer"
sport = "Tennis"
achievements = 20

if sport == "Tennis" or achievements == 21:
    print(f"{player1} plays tennis and has {achievements} achievements")
else: print(f"{player1} does not fulfill these criteria")

# Quiz 3: Write a Python program to check if a player has less than 10 achievements
# and does not play Soccer. Print their details if they meet the criteria.

player3 = "Usain Bolt"
achievements = 8
sport = "Athletics"
if achievements < 10 and sport != "Soccer":
    print(f"{player3} plays {sport} and has {achievements} achievements")
else: print(f"{player3} does not fulfill the criteria")

