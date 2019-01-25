'''
print("smith\exam1\test.txt")
print("smith\\exam1\\test.txt")
x = "Programming is fun"
print(x.find('ram'))

x = 2+9*((3*12)-8)/10
print(x)
print(bool('False')) ; print(bool())
i = 1
while True:
    if i%7 == 0:
        break
    print(i)
    i += 1
x = 'abcd'
for i in range(len(x)):
    x[i].upper()
print (x)
for i in [1, 2, 3, 4][::-1]:
    print (i, end =' ')
example = "snow world"
print("%s" % example[4:7])

class Count:
    def __init__(self, count = 0):
       self.__count = count

c1 = Count(2)
c2 = Count(2)
print(id(c1) == id(c2), end = " ")
s1 = "Good"
s2 = "Good"
print(id(s1) == id(s2))
x = [3, 4, 5, 20, 5, 25, 1, 3]
x.pop()
print(x)
m = [[x, x + 1, x + 2] for x in range(0, 3)]
print(m)
a={1:"A",2:"B",3:"C"}
for i,j in a.items():
    print(i,j,end=" ")

def foo(k):
    k = [1]
q = [0]
foo(q)
print(q)

class test:
     def __init__(self,a="Hello World"):
         self.a=a

     def display(self):
         print(self.a)
obj=test()
obj.display()

class py_solution:
    def twoSum(self, nums, target):
        return_index = []
        print(range(len(nums)))
        for n in range(len(nums)):
            print(n)
            com = target - nums[n]
            if(com in nums and nums.index(com) != n):
                return_index = [n, nums.index(com)]
                break

        if(n == len(nums) - 1 and return_index == []):
            return_index = "No two sums"
        return return_index
   def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            print(parenthese,":",stack)
            if parenthese in pchar:
                stack.append(parenthese)
                print("if:",stack)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

def romanToInt(s):
    num, pre = 0, 1000
    for i in [map[j] for j in s]:
        print(i,num,pre)
        num, pre = num + i - 2*pre if i > pre else num + i, i
        print("a",i,num,pre)
    return num#print(py_solution().is_valid_parenthese("()"))

print(romanToInt('IV'))

#location=42.349018433310675%2C-71.09757458041415
import requests
#Consumer Key: uHAHSZCPD6gFAF4b9xnsvCfcpXA6tREQ
resp = requests.get('https://apis.solarialabs.com/shine/v1/total-home-scores/reports')
#print(resp.headers)


import requests
import json
params = (
    ('lat', '42.349018433310675'),
    ('lon', '-71.09757458041415'),
    ('apikey', 'uHAHSZCPD6gFAF4b9xnsvCfcpXA6tREQ'),
)

resp = requests.get('https://apis.solarialabs.com/shine/v1/total-home-scores/reports', params=params)
data = resp.json()
#print (data)

for val in data["totalHomeScores"]["traffic"]:
        #print (*(list(str(data["totalHomeScores"]["traffic"][val]))),sep = '')
        print ((data["totalHomeScores"]["traffic"][val]))

#print(data["totalHomeScores"]["traffic"]["value"])

from flask import Flask
from flask import send_from_directory
import os

static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')
#print(static_file_dir)
app = Flask(__name__)
#@app.route('/')
#def hello_world():
#    return 'Hello, World!'
#
#@app.route('/dir', methods=['GET'])
#def serve_dir_directory_index():
#    return send_from_directory(/Users/arun/Downloads/Python Assignments/, 'CS521_hm_6.docx')
#
#
#@app.route('/dir/<path:path>', methods=['GET'])
#def serve_file_in_dir(path):
#
#    if not os.path.isfile(os.path.join(static_file_dir, path)):
#        path = os.path.join(path, 'CS521_hm_6.docx')
#
#    return send_from_directory(static_file_dir, path)
#

# Routes
@app.route('/',methods=['GET'])
def root():
  return send_from_directory(static_file_dir,'xyz.mp3')

if __name__ == "__main__":
    #app.run()
    app.run(host='0.0.0.0', port=8000)





#app.run(host='0.0.0.0',port=8080)

from operator import itemgetter
import itertools
student_course_pairs = [
    ["58", "Software Design"],
    ["58", "Linear Algebra"],
    ["94", "Art History"],
    ["94", "Operating Systems"],
    ["17", "Software Design"],
    ["58", "Mechanics"],
    ["58", "Economics"],
    ["17", "Linear Algebra"],
    ["17", "Political Science"],
    ["94", "Economics"]
]
#print(student_course_pairs[0][0])
#for x in student_course_pairs:
#    print(x[0])
#newlist = [[y[0] for y in student_course_pairs if y[1]==x] for x in courses]
#n = [[y[1] for y in student_course_pairs if y[1]==x] for x in courses]
#print(courses)
#print(newlist,":",n)
#print(dict(newlist,n))
#j = [*newlist,*n]
#d = zip(newlist,n)
#print(dict(d))
#
def check(lst):
    crs = []
    for x in student_course_pairs:
        if lst[0] == x[0]:
            crs.append(x[1])
    stu = []
    pr = []
    #print(crs)
    n = [[y[1] for y in student_course_pairs if y[1]==x and y[0] != lst[0]] for x in crs]
    r = [[y[0] for y in student_course_pairs if y[1]==x] for x in [j for sub in n for j in sub]]
    q = [j for sub in n for j in sub]
    s = list(set([a[1] for a in r]))
    for d in range(len(s)):
        for f in range(len(q)):
            for y in student_course_pairs:
                #print (q[f],s[d],":",y[0],y[1])
                if y[1] == q[f] and y[0] == s[d]:
                    pr.append(y)
    for z in range(len(pr)):
        pr[z].append(lst[0])
    #print (pr)
    for d, g in itertools.groupby(pr, key=itemgetter(0)):
        print (lst[0],d,":",[entry[1] for entry in g])


#    rslt = []
#    courses = set(map(lambda x:x[1], student_course_pairs))
#    for lst[1] in student_course_pairs[1]:
#        print(student_course_pairs[])

if __name__ == '__main__':
    check(["58", "Software Design"])
    t = []
    for d, g in itertools.groupby(student_course_pairs, key=itemgetter(0)):
        t.append(list([d]+[entry[1] for entry in g]))
    print(t)
    #for d, g in itertools.groupby(t, key=itemgetter(0)):
    #    print(d,[entry for entry in g])





def generate_ranks(sales_data):
    sorted_data = sorted(sales_data, key=itemgetter(0, 2))
    print(sorted_data)
    for date, group in itertools.groupby(sorted_data, key=itemgetter(0)):
        yield [date] + [entry[1] for entry in group]


if __name__ == '__main__':
    sales_data = [
        [201703, 'Bob', 3000],
        [201703, 'Sarah', 6000],
        [201703, 'Jim', 9000],
        [201704, 'Bob', 8000],
        [201704, 'Sarah', 7000],
        [201704, 'Jim', 12000],
        [201705, 'Bob', 15000],
        [201705, 'Sarah', 14000],
        [201705, 'Jim', 8000],
        [201706, 'Bob', 10000],
        [201706, 'Sarah', 18000],
    ]
    sales_ranks = list(generate_ranks(sales_data))
    print(sales_ranks)

if __name__ == '__main__':
    s ='aAaBbcCdE'
    print(sorted(sorted(s), key=str.upper))
    print(x)

graph1 = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}

def all_palindromes(inp):
    count = 0;
    for idx, char in enumerate(inp):

        start = idx - 1
        end =  idx + 1
        while start >= 0 and end < len(inp) and inp[start] == inp[end]:
            count += 1
            start -= 1
            end += 1

        start = idx
        end =  idx + 1
        while start >= 0 and end < len(inp) and inp[start] == inp[end]:
            count +=1
            start -= 1
            end += 1
    print("c",count+len(inp))

all_palindromes('hellolle')

class Solution:
    def dfs(self, grid, i, j):
        print("enter i:",i,"j:",j)
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            print("break i:",i,"j:",j)
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        print("a i:",i,"j:",j)
        self.dfs(grid, i-1, j)
        print("b i:",i,"j:",j)
        self.dfs(grid, i, j+1)
        print("c i:",i,"j:",j)
        self.dfs(grid, i, j-1)
        print("d i:",i,"j:",j)

    def numIslands(self, grid):

        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        count = 0
        print(range(len(grid)),":",range(len(grid[0])))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    print("call",i,j)
                    self.dfs(grid, i, j)
#                    count += 1
#        #return count
#        print (count)

Solution().numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])

import sys


class Node:
    def __init__(self, data):
        #print(data)
        self.data = data
        self.left = None
        self.right = None
        self.nextRight = None

    def __str__(self):
        return '{}'.format(self.data)


def printLevelByLevel(root):
    # print level by level
    if root:
        node = root
        while node:
            print('{}'.format(node.data), end=' ')
            node = node.nextRight
        print()
        if root.left:
            printLevelByLevel(root.left)
        else:
            printLevelByLevel(root.right)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)


def connect(root):
    # set nextRight of all nodes of a tree
    queue = []
    queue.append(root)
    # null marker to represent end of current level
    queue.append(None)
    # do level order of tree using None markers
    while queue:
        p = queue.pop(0)
        print(p)
        if p:
            # next element in queue represents
            # next node at current level
            print(len(queue)," ",queue[0])
            p.nextRight = queue[0]
            # pus left and right children of current node
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)
        elif queue:
            queue.append(None)


def main():
    """Driver program to test above functions.
        Constructed binary tree is
                10
               /  \
             8      2
            /        \
          3            90
    """

    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.right.right = Node(90)
    connect(root)

if __name__ == "__main__":
    main()

def areMetaStrings( str1, str2) :
    len1 = len(str1)
    len2 = len(str2)

    # Return false if both are not of equal length
    if (len1 != len2) :
        return False

    # To store indexes of previously mismatched
    # characters
    prev = -1
    curr = -1

    count = 0
    i = 0
    while i < len1 :

        # If current character doesn't match
        if (str1[i] != str2[i] ) :

        # Count number of unmatched character
            count = count + 1

            # If unmatched are greater than 2,
            # then return false
            if (count > 2) :
                return False

            # Store both unmatched characters of
            # both strings
            prev = curr
            curr = i

        i = i + 1
        print(prev,":",curr)

    # Check if previous unmatched of string1
    # is equal to curr unmatched of string2
    # and also check for curr unmatched character,
    # if both are same, then return true
    return (count == 2 and str1[prev] == str2[curr]
               and str1[curr] == str2[prev])

# Driver method
str1 = "converse"
str2 = "conserve"
if ( areMetaStrings(str1,str2) ) :
     print ("Yes")
else:
    print ("No")
s = "add"
t = "eg"
x = zip(s,t)
print(len(set(s)),":",set(t),":",set(zip(s,t)))
print(len(set(zip(s, t))) == len(set(s)) == len(set(t)))
d1, d2 = {}, {}
from collections import Counter
q = Counter(s)
print(q)
for i, val in enumerate(s):
    print(i,":",val,":",d1.get(val, []))
    d1[val] = d1.get(val, []) + [i]
    print()
    print(d1.values())

def findPlatform(S,E):

    if len(S) != len(E):
        return -1

    S.sort()
    E.sort()

    currChairs = 1
    minChairs = 1
    size = len(S)
    i = 1
    j = 0

    while (i < size and j < size):

        if (S[i] < E[j]):
            currChairs+=1
            i+=1

            if (currChairs > minChairs):
                minChairs = currChairs
        else:

            currChairs-=1
            j+=1

    return minChairs


S = [1,2,6,5,3]
E = [5,5,7,6,8]
#
print("Minimum Number of Platforms Required = ",
        findPlatform(S, E))
'''
import math
X = [-1,2,-4,2,4]
Y = [1, 2,-4,2,-1]
D = dict(zip(X, Y))
dist = []
i = 0
while i < len(X):
    res = (math.sqrt((X[i]*X[i]) + (Y[i]*Y[i])))
    dist.append(math.floor(res))
    print(res)    i+= 1
y = dist.sort()
print(sorted(dist)[0])

#dist=[]
#for x,y in D.items():
#    a = math.sqrt(x*x + y*y)
#    print(a)
