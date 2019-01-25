"""
CS 521 Information Structures with Python
#########################################
Module          - HW 5
Creation Date   - 10/17/2018
Student Name    - Gautam Gowrishankar

"""
def footToMeter(foot):
   return foot*0.305

def meterToFoot(meter):
   return meter/0.305

mtr = 20
print ("Feet \t         Meters  \t Meters \t Feet")
for f in range(1,11):
   print("%1.1f \t \t %1.3f \t | \t %1.1f \t\t %1.3f" % (f,footToMeter(f),mtr,meterToFoot(mtr)))
   if (f % 2 == 0):
       mtr += 4;
   else:
       mtr += 6;

print("\n -End of Program- ")
