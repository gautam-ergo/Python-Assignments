"""
CS 521 Information Structures with Python
#########################################
Module          - HW 4
Creation Date   - 10/10/2018
Student Name    - Gautam Gowrishankar

"""
def main():
# Students' answers to the questions
     answers = [
         ['A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
         ['D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'],
         ['E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'],
         ['C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'],
         ['A', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
         ['B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
         ['B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
         ['E', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D']]

     # Key to the questions
     keys = ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D']
     stu = []
     count = []

     # Grade all answers
     for i in range(len(answers)):
     # Grade one student
         correctCount = 0
         for j in range(len(answers[i])):
             if answers[i][j] == keys[j]:
                 correctCount += 1
         print("Student", i, "'s correct count is", correctCount)
         stu.append(i)
         count.append(correctCount)
     # Combine students and their scores
     data = dict(zip(stu,count))
     result = sorted(data.items() , key=lambda t : t[1] , reverse=True)
     print("\nSorting by Correct count - \n")
     for s,c in result:
         print("Student", s, "'s correct count is", c)
main()
print("\n -End of Program- ")
