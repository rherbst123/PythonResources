#  4. High Score
#  Assume that a file named scores.txt exists on the computer’s disk. It contains a series of 
# records, each with two fields – a name, followed by a score (an integer between 1 and 100). 
# Write a program that displays the name and score of the record with the highest score, as 
# well as the number of records in the file. (Hint: Use a variable and an “if” statement to 
# keep track of the highest score found as you read through the records, and a variable to 
# keep count of the number of records.)


def scores(roster):
    # Initialize variable to store the highest score found
    highScore = 0
    # Initialize variable to store the name of the person with the highest score
    scorer = ""
    # Initialize counter to keep track of the number of records
    records = 0

    # Open the file containing the scores
    roster = open(roster)
    
    #Optional for getting full roster
 


    # Iterate through each line in the file
    for lines in roster:
        # Increment the record counter for each line
        records += 1
        # Split the line into name and score, removing any extra whitespace
        name, score = lines.strip().split()
        # Convert the score from string to integer
        score = int(score)
        # Check if the current score is higher than the highest score found so far
        if score > highScore:
            # Update the highest score
            highScore = score
            # Update the name of the person with the highest score
            scorer = name
    
    # Print the name of the person with the highest score and their score
    print(scorer, highScore)

    




def main():
    roster = "Chapter6//scores.txt"
    scores(roster)
main()
