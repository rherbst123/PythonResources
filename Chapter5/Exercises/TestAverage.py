#  15. Test Average and Grade
#  Write a program that asks the user to enter five test scores. The program should display a 
# letter grade for each score and the average test score. Write the following functions in the 
# program:
#  •	calc_average. This function should accept five test scores as arguments and return the 
# average of the scores.
#  •	determine_grade. This function should accept a test score as an argument and return 
# a letter grade for the score based on the following grading scale:


def main():
    scores = []
    numOfTests = int(input("How many tests are being graded today?: "))
    for counter in range(numOfTests):
        score = int(input(f"Enter test score for test[{counter + 1}] "))
        scores.append(score)
        
    #print(scores)
    
    
    print(f"The avgerage of the tests are: {calc_average(scores, numOfTests)}")
    print("Below is a list of all tests:")
    print
    print(determine_grade(scores))
    


def calc_average(scores, numOfTests):
    totalScores = sum(scores)
    average = totalScores // numOfTests
    
    return average



def determine_grade(scores):
    for score in scores:
        if score < 60:
            print(f"{score}% = F")
        if score > 59 and score < 70:
            print(f"{score}% = D")
        if score > 69 and score < 80:
            print(f"{score}% = C")
        if score > 79 and score < 90:
            print(f"{score}% = B")
        if score > 89:
            print(f"{score}% = A")
            
        
     
     #return grade


main()