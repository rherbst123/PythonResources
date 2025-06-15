# 9.  Population Data
# If  you  have  downloaded  the  source  code  you  will  find  a  file  named  USPopulation.txt 
# in the Chapter 07 folder. The file contains the midyear population of the United States, in 
# thousands, during the years 1950 through 1990. The first line in the file contains the popu-
# lation for 1950, the second line contains the population for 1951, and so forth.
# Write a program that reads the file’s contents into a list. The program should display the 
# following data:
# •  The average annual change in population during the time period
# •  The year with the greatest increase in population during the time period
# •  The year with the smallest increase in population during the time period



def average(average):
    differences = []
    for i in range(len(average) - 1):
        k = average[i + 1] - average[i]
        differences.append(k)
    
    print("Annual differences:", differences)
    print("Average annual change:", sum(differences) / len(differences))
    print("Greatest increase in population:", max(differences))
    print("Smallest increase in population:", min(differences))





def main():
    with open('C:\\Users\\Riley\\Documents\\GitHub\\RileyPython\\Chapter7\\Extra_Files\\USPopulation.txt', 'r') as population_data:
        population_list = [int(line.strip()) for line in population_data]
    print(population_list)
    average(population_list)


main()