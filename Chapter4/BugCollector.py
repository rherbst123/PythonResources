"""  1. Bug Collector
 A bug collector collects bugs every day for five days. Write a program that keeps a running  
total of the number of bugs collected during the five days. The loop should ask for the  
number of bugs collected for each day, and when the loop is finished, the program should 
display the total number of bugs collected. """

days = 5
bugs = 0
for counter in range(5):
    bugsDay = int(input("How many bugs?: "))
    bugs += bugsDay

print("You found",bugs,"bugs!")
