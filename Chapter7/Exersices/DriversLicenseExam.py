# 7.   Driver’s License Exam
# The local driver’s license office has asked you to create an application that grades the writ-
# ten portion of the driver’s license exam. The exam has 20 multiple-choice questions. Here 
# are the correct answers:
# 1.  A
# 2.  C
# 3.  A
# 4.  A
# 5.  D
# 6.  B
# 7.  C
# 8.  A
# 9.  C
# 10.  B
# 11.  A
# 12.  D
# 13.  C
# 14.  A
# 15.  D
# 16.  C
# 17.  B
# 18.  B
# 19.  D
# 20.  A
# Your  program  should  store  these  correct  answers  in  a  list.  The  program  should  read  the   
# student’s  answers  for  each  of  the  20  questions  from  a  text  file  and  store  the  answers  in  
# another list. (Create your own text file to test the application.) After the student’s answers 
# have been read from the file, the program should display a message indicating whether the 
# student passed or failed the exam. (A student must correctly answer 15 of the 20 questions 
# to pass the exam.) It should then display the total number of correctly answered questions, 
# the total number of incorrectly answered questions, and a list showing the question num-
# bers of the incorrectly answered questions.


def main():
    correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
    
    filename = "/home/riley/Documents/GitHub/RileyPython/Chapter7/Extra_Files/driving_exam.txt"
    with open(filename, 'r') as file:
        student_answers = [line.strip().upper() for line in file if line.strip()]
    
    if len(student_answers) != 20:
        print("Error: The file must contain exactly 20 answers.")
        return

    correct_count = 0
    incorrect_questions = []

    for index, (correct, student) in enumerate(zip(correct_answers, student_answers), start=1):
        if student == correct:
            correct_count += 1
        else:
            incorrect_questions.append(index)

    incorrect_count = 20 - correct_count

    if correct_count >= 15:
        print("Student passed the exam.")
    else:
        print("Student failed the exam.")

    print("Total correct answers:", correct_count)
    print("Total incorrect answers:", incorrect_count)
    if incorrect_questions:
        print("Questions answered incorrectly:", incorrect_questions)

if __name__ == "__main__":
    main()