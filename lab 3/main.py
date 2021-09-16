
# List of lists
a = [["windows", "mac"], ["portable executable", "mac-0"]]
print(a[0][1]) # what list, and what place

# creating multiple filled lists
b = [[0]*3 for i in range(3)]
c = [0]*3, [0]*3, [0]*3

# 3 dimensional
d = [[[0]*3 for i in range(3)] for j in range(3)]

# Going through matrices with two for loops

# Default values. Check if it can be done at the beginning or only at the end
# Or  if every argument have to have default value
# SyntaxError: non-default argument follows default argument

# *data, any given arguments. ** dictionary
def SayHello(*data):
    print("hei hei"+data[1])

# SayHello("hei", "du")

# Defining functions in functions

def saywelcome(data):
    for i,j in data.items():
        print(f"welcome to {j}" )
        print(f"hey {i}")

input = {"stine":"Acit", "cam":"acit2"}

def transpose(m):
    rowcount = len(m)
    colcount = len(m[0]) # Sjekker antall kolonner i hver rad ved å sjekke én rad
    t = [[0]*colcount for i in range(rowcount)]
    for i in range (rowcount):
        for j in range(colcount):
            t[i][j] = m[j][i]
    return t

#m1 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

#m1 = [[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,5]]
m2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

# multiplying matrices
# nr of colums in the first matrix must be equal to the rows in the second

def Multiply(m1,m2):
    rowcount1 = len(m1)
    colcount1 = len(m1[0])
    rowcount2 = len(m2)
    colcount2 = len(m2[0])
    if colcount1 != rowcount2: return "wrong input"
    c = [[0]*colcount2 for i in range(rowcount1)]
    for i in range(rowcount1):
        for j in range(colcount2):
            c[i][j] = 0
            for k in range(colcount1):
                c[i][j] = m1[i][k] * m2[k][j]
    return c

m1 = [[1,2,3],[4,5,6],[7,8,9]]

# Recursion for å håndtere en enda større matrise(?)













