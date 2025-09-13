# 7.  Grade Calculator
# A class has two tests worth 25 points each along with a main exam worth 50 points. For a stu-
# dent to pass the class, they must obtain an overall score of at least 50 points, and must obtain at 
# least 25 points in the main exam. If a student’s total score is less than 50 or they obtain less than 
# 25 points in the main exam, they receive a grade of “Fail”. Otherwise, their grade is as follows: 
# If they get more than 80, they get a grade of “Distinction”. 50–59 = “Pass”.
# If they get less than 80 but more than 60, they get a “Credit” grade.
# If they get less than 60, they get a ”Pass” grade.
# Write a program that prompts the user to enter their points for both tests and the exam and 
# converts the values to integers. The program should first check if the points entered for the 
# tests and exam are valid. If any of the test scores are not between 0 and 25, or the exam 
# score is not between 0 and 50, the program should display an error message. Otherwise, 
# the program should display the total points and the grade.

test1 = int(input("Enter score for Test 1: "))
if test1 < 0 or test1 > 25:
    print("Error")

test2 = int(input("Enter score for Test 2: "))
if test2 < 0 or test1 > 25:
    print("Error")

mainExam = int(input("Enter score for the Main Exam: "))
if mainExam < 0 or test1 > 50:
    print("Error")

print(f"The students scores are {test1} / 25, {test2} / 25, {mainExam} / 50")


total = test1 + test2 + mainExam

if total >= 50 and mainExam >= 25:
    print("You have passed the class!")
    if total >= 80:
        print("Passed with Distinction")
    elif total < 80 or total > 60:
        print("Passed with Credit")
    elif total < 60:
        print("Passed")

if total < 50 and mainExam < 25:
    print("You have Failed the class :( ")


