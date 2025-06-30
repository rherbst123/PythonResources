# 13.  Magic 8 Ball
# Write a program that simulates a Magic 8 Ball, which is a fortune-telling toy that displays a 
# random response to a yes or no question. In the student sample programs for this book, you 
# will  find  a  text  file  named  8_ball_responses.txt.  The  file  contains  12  responses,  such  
# as “I don’t think so”, “Yes, of course!”, “I’m not sure”, and so forth. The program should 
# read the responses from the file into a list. It should prompt the user to ask a question, then 
# display one of the responses, randomly selected from the list. The program should repeat 
# until the user is ready to quit.
import random

while True:
    ball = open("Chapter7/Extra_Files/8Ball.txt", 'r', encoding="utf-8")
    lines = ball.readlines()

    print("What is your question for the allmighty 8 Ball?:")



    question = input("Question: ")
    line_number = random.randint(1,12)
    print(lines[line_number - 1].strip())
    end = input("Are you done?: (y/n) ")
    
    if end == "y":
        exit()
    if end == "n":
        continue
    else:
        print("please enter a y or an n")
        

    