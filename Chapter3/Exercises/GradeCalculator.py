"""  A class has two tests worth 25 points each along with a main exam worth 50 points. For a stu
dent to pass the class, they must obtain an overall score of at least 50 points, and must obtain at 
least 25 points in the main exam. If a student’s total score is less than 50 or they obtain less than 
25 points in the main exam, they receive a grade of “Fail”. Otherwise, their grade is as follows: 
If they get more than 80, they get a grade of “Distinction”. 50–59 = “Pass”.
 If they get less than 80 but more than 60, they get a “Credit” grade.
 If they get less than 60, they get a ”Pass” grade.
 Write a program that prompts the user to enter their points for both tests and the exam and 
converts the values to integers. The program should first check if the points entered for the 
tests and exam are valid. If any of the test scores are not between 0 and 25, or the exam 
score is not between 0 and 50, the program should display an error message. Otherwise, 
the program should display the total points and the grade. """

test1 = int(25)
test2 = int(25)
final = int(50)

testGrade1 = int(input("Enter score for test 1 (Out of 25): "))
testGrade2 = int(input("Enter score for test 2 (Out of 25): "))
finalGrade = int(input("Enter score for final test (Out of 50): "))

finalScore = testGrade1 + testGrade2 + finalGrade
#print("Student has a score of: ", finalScore)


if finalGrade < 26:
    print("student has failed with a final grade score of: ", finalGrade)

if finalScore < 50:
    print("Student failed with score of: ", finalScore)

if finalScore > 80:
    print("Student passes with a score of: ", finalScore)

if finalScore < 80:
    if finalScore > 60:
        print("Student gets a 'Credit' grade of:", finalScore)

if finalScore < 60:
    print("Student gets a pass with score: ", finalScore)