# 1.  Bug Collector
# A bug collector collects bugs every day for five days. Write a program that keeps a running  
# total  of  the  number  of  bugs  collected  during  the  five  days.  The  loop  should  ask  for  the   
# number of bugs collected for each day, and when the loop is finished, the program should 
# display the total number of bugs collected


total_bugs = 0
days = int(input("How many days will you be collecting?: "))



for i in range(1, days + 1):
    daily_bugs = int(input(f"Enter the bug count for day: {i}: "))
    total_bugs += daily_bugs

print(f"On the final day you have collected a total of {total_bugs} bugs")