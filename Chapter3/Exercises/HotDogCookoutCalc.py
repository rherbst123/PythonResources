""" 
8. Hot Dog Cookout Calculator
 Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8. Write a 
program that calculates the number of packages of hot dogs and the number of packages of 
hot dog buns needed for a cookout, with the minimum amount of leftovers. The program 
should ask the user for the number of people attending the cookout and the number of hot 
dogs each person will be given. The program should display the following details:
 •	The	minimum	number	of	packages	of	hot	dogs	required
 •	The minimum number of packages of hot dog buns required
 •	The number of hot dogs that will be left over
 •	The number of hot dog buns that will be left over 

"""
people = int(input('Please enter the number of people attending the cookout: '))
hotdogs = int(input('Please enter the number of hot dogs each person will be given: '))

if people * hotdogs % 8 == 0 and people * hotdogs % 10 == 0:
    print(people * hotdogs // 8, 'of packages of hot dog buns required.')
    print(people * hotdogs // 10, 'of packages of hot dogs required.')
    print('The number of hot dog buns that will be left over is 0')
    print('The number of hot dogs that will be left over is 0')
elif people * hotdogs % 8 == 0 and people * hotdogs % 10 != 0:
    print(people * hotdogs // 8, 'of packages of hot dog buns required.')
    print(people * hotdogs // 10 + 1, 'of packages of hot dogs required.')
    print('The number of hot dog buns that will be left over is', people * hotdogs % 8)
    print('The number of hot dogs that will be left over is', 
         (people * hotdogs // 10 + 1) * 10 - people * hotdogs)  
elif people * hotdogs % 8 != 0 and people * hotdogs % 10 == 0:
    print(people * hotdogs // 8 + 1, 'of packages of hot dog buns required.')
    print(people * hotdogs // 10, 'of packages of hot dogs required.')
    print('The number of hot dog buns that will be left over is',
         (people * hotdogs // 8 + 1) * 8 - people * hotdogs)
    print('The number of hot dogs that will be left over is', people * hotdogs % 10)
else:
    print(people * hotdogs // 8 + 1, 'of packages of hot dog buns required.')
    print(people * hotdogs // 10 + 1, 'of packages of hot dogs required.')
    print('The number of hot dog buns that will be left over is',
         (people * hotdogs // 8 + 1) * 8 - people * hotdogs)
    print('The number of hot dogs that will be left over is',
         (people * hotdogs // 10 + 1) * 10 - people * hotdogs) 