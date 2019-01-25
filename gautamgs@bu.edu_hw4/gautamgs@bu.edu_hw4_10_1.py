"""
CS 521 Information Structures with Python
#########################################
Module          - HW 4
Creation Date   - 10/10/2018
Student Name    - Gautam Gowrishankar

"""

#For Displaying the current version of Python
import platform
print ("Python version being used for this code - ", platform.python_version(),'\n')

try:
    scores = [int(x) for x in input("Enter Scores (separated by space): ").split(" ")]
    if scores != []:
        top_score = max(scores)
        for x in scores:
            if x >= top_score - 10:
                print("Student", scores.index(x), "score is", x, "and grade is A")
            elif x >= top_score - 20:
                print("Student", scores.index(x), "score is", x, "and grade is B")
            elif x >= top_score - 30:
                print("Student", scores.index(x), "score is", x, "and grade is C")
            elif x >= top_score - 40:
                print("Student", scores.index(x), "score is", x, "and grade is D")
            else:
                print("Student", scores.index(x), "score is", x, "and grade is F")
except:
    print("Please Enter Valid Scores ")

print("\n -End of Program- ")
