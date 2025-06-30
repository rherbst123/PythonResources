# 0.  World Series Champions
# If you have downloaded the source code you will find a file named WorldSeriesWinners.
# txt in the Chapter 07 folder. This file contains a chronological list of the World Series win-
# ning teams from 1903 through 2009. (The first line in the file is the name of the team that 
# won in 1903, and the last line is the name of the team that won in 2009. Note the World 
# Series was not played in 1904 or 1994.)
# Write a program that lets the user enter the name of a team, then displays the number of 
# times that team has won the World Series in the time period from 1903 through 2009


def main():
    with open(r'/home/riley/Documents/GitHub/RileyPython/Chapter7/Extra_Files/WorldSeriesWinners.txt', 'r') as world_series:
        world_series_list = [line.strip() for line in world_series]
    team = input("Enter the name of a team: ")
    count = 0
    for i in range(len(world_series_list)):
        if world_series_list[i] == team:
            count += 1
    print(f"The {team} won {count} times between 1903 and 2009")


main()


