#  10. Golf Scores
#  The Springfork Amateur Golf Club has a tournament every weekend. The club president 
# has asked you to write two programs:
#  1. A program that will read each player’s name and golf score as keyboard input, then 
# save these as records in a file named golf.txt. (Each record will have a field for the 
# player’s name and a field for the player’s score.)
#  2. A program that reads the records from the golf.txt file and displays them.

print("Welecome to the game of golf, enter your names and your scores")

golf_sheet = open("Chapter6/golf.txt", "w")


number_of_players = int(input("How many people are playing today?: "))



for i in range(number_of_players):
    name = input("Enter a name: ")
    score = input("Enter the score for {}: ".format(name))
    golf_sheet.write(name + "," + score+ "\n")
golf_sheet.close()
print("Player names and scores have been saved to golf.txt.")

