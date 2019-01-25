"""
CS 521 Information Structures with Python
#########################################
Module          - HW 7
Creation Date   - 11/07/2018
Student Name    - Gautam Gowrishankar

"""
def sumMajorDiagonal():
    inp = []
    sum = 0
    for f in range(4):
        rows = [float(x) for x in input("Enter a 4-by-4 matrix for row " + str(f)+" (separated by space):").split(" ")]
        inp.append(rows)
        sum = sum + inp[f][f]
    return print ("Sum of the elements in the major diagonal is - ",sum)

if __name__ == "__main__":
    try:
        sumMajorDiagonal()
    except Exception as e:
        print("Error - ",str(e))
    finally:
        print("\n -End of Program- ")
