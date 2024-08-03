import sys
sys.setrecursionlimit(1000)

#board generator
def printboard(a):
    for y in range(0 , 9):
        s=""
        for x in range(0 , 9):
            s = s + str(a[y][x]) + " "
        print(s)

#Takes in a list of numbers.
#return true if there is no duplicates, false if there is duplicates.
def checkdifferent(a):
    for x in range(0 , len(a)):
        for y in range((x+1) , len(a)):
            if a[x] == a[y]:
                return False
    else:
        return True

#this function checks a 3 by 3 square , if there are no duplicates , false if there are duplicates.
def square(a , row , col):
    d = []
    if (row >= 0) and (row <= 2):
        r = [0,1,2]
    elif (row >= 3) and (row <= 5) :
        r = [3,4,5]
    elif (row >= 6) and (row <= 8) :
        r = [6,7,8]
    if (col >= 0) and (col <= 2):
        c = [0,1,2]
    elif (col >= 3) and (col <= 5):
        c = [3,4,5]
    elif (col >= 6) and (col <= 8):
        c = [6,7,8]     
    for k in range(0 , 3):
        for e in range(0 , 3):
            if (a[r[k]][c[e]] != 0):
                d.insert(0 , a[r[k]][c[e]])
    if (checkdifferent(d) == False):        
        return False
    else:
        return True

#take in suduku board. returns true if all conditions are satisfied else returns false.               
def checkboard(a , value , row , col):
    d = []
    m = []
    a[row][col] = value
    for x in range(0 , 9):
        if (a[row][x] != 0):
            m.insert(len(m) , a[row][x])
    if (checkdifferent(m) == False):
        return False
    for x in range(0 , 9):
        if (a[x][col] != 0):
            d.insert(len(d) , a[x][col])
    if (checkdifferent(d) == False):
        return False
    if (square(a , row , col) == False):
        return False
    return True

#looks for an empty cell(0)
def emptycellchecker(a):
    for x in range(0 , 9):
        for y in range(0, 9):
            if a[x][y] == 0 :
                return [x , y]
    return True

def solvesudoku(a):

    empty = emptycellchecker(a)
    if emptycellchecker(a) == True:
        #return True
        print(a)
    else:
        row = empty[0]
        column = empty[1]
        for guess in range(1,10):
            if checkboard(a , guess , row , column):
                a[row][column] = guess
                if solvesudoku(a):
                    return True
            a[row][column] = 0

        return False

    

a = [[0 , 0 , 0, 5, 0, 3, 6, 9, 0],
     [4 , 0 , 0, 6, 2, 0, 0, 0, 7],
     [0 , 0 , 0, 4, 0, 0, 0, 2, 0],
     [0 , 6 , 9, 0, 0, 2, 4, 0, 0],
     [1 , 0 , 0, 0, 3, 0, 0, 0, 8],
     [0 , 0 , 4, 9, 0, 0, 5, 1, 0],
     [0 , 8 , 0, 0, 0, 6, 0, 0, 0],
     [6 , 0 , 0, 0, 4, 5, 0, 0, 9],
     [0 , 4 , 5, 2, 0, 1, 0, 0, 0]]

answer=[[2 , 7 , 8 , 5 , 1 , 3 , 6 , 9 , 4],
        [4 , 1 , 3 , 6 , 2 , 9 , 8 , 5 , 7],
        [5 , 9 , 6 , 4 , 8 , 7 , 3 , 2 , 1],
        [8 , 6 , 9 , 1 , 5 , 2 , 4 , 7 , 3],
        [1 , 5 , 2 , 7 , 3 , 4 , 9 , 6 , 8], 
        [7 , 3 , 4 , 9 , 6 , 8 , 5 , 1 , 2],
        [9 , 8 , 1 , 3 , 7 , 6 , 2 , 4 , 5],
        [6 , 2 , 7 , 8 , 4 , 5 , 1 , 3 , 9],
        [3 , 4 , 5 , 2 , 9, 1 , 7 , 8 , 6]]

(solvesudoku(a))

