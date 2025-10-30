# 13.  Magic 8 Ball
# Write a program that simulates a Magic 8 Ball, which is a fortune-telling toy that displays a 
# random response to a yes or no question. In the student sample programs for this book, you 
# will  find  a  text  file  named  8_ball_responses.txt.  The  file  contains  12  responses,  such  
# as “I don’t think so”, “Yes, of course!”, “I’m not sure”, and so forth. 
# 
# The program should 
# read the responses from the file into a list. It should prompt the user to ask a question, then 
# display one of the responses, randomly selected from the list. The program should repeat 
# until the user is ready to quit
import random

while True:
    ballResponses = open("/home/riley/Documents/GitHub/RileyPython/Chapter7/Extra_Files/8Ball.txt", "r") 
    responses = ballResponses.readlines()

    userQuestion = input("What question do you have?: ")

    line_number = random.randint(1,12)
    print(responses[line_number - 1].strip())
    chooseToEnd = input("Are you done?: ")

    if chooseToEnd == "y":
        break
    if chooseToEnd == "n":
        continue
    else:
        print("Please put y or n")

    

