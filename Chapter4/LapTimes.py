""" 3. Lap Times
 Write a program that asks the user to enter the number of times that they have run around 
a racetrack, and then uses a loop to prompt them to enter the lap time for each of their laps. 
When the loop finishes, the program should display the time of their fastest lap, the time of 
their slowest lap, and their average lap time. """

laps = int(input("How many times you gonna run that hoe?: "))
times = []
total = 0.0

for counter in range(laps):
    time = float(input("What was the time for this lap? (1.43) = 1:43: "))
    times.append(time)
    total += time

print("Times in order of ran",times)

times = sorted(times, key=float)

#print(times) 
# #SortedTimes

fastest = times[laps - laps]
print("Your fastest lap is: ", fastest)

slowest = times[laps-1]
print("Your slowest lap is: ", slowest)

avgerage = total / laps
print("Avgerage time is: ", avgerage)
