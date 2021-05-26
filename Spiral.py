#  File: Spiral.py

#  Description: Create Ulam's spiral and sum the value around input value

#  Student Name: Samuel Lee

#  Student UT EID: STL467

#  Partner Name: Yuro Sato

#  Partner UT EID: YS9434

#  Course Name: CS 313E

#  Unique Number: 52240

#  Date Created: 1/28/2021

#  Date Last Modified: 1/28/2021

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n

import sys

def create_spiral(n):

    #creating 2dimensional arrays of spiral
    spiral = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        spiral.append(row)

    #initial position
    spiral[n//2][n//2] = 1

    start_pt = [n//2, n//2]

    # populates spiral
    for level in range(1,n):
        if level % 2 == 0:
            start_pt = even(spiral, start_pt, level)
        else:
            start_pt = odd(spiral, start_pt, level)

    return spiral

# movement of case of odd level
def odd(spiral, start_pt, level):
    begin = (level ** 2) + 1 # next number
    # move 1 to right
    row = start_pt[0]
    col = start_pt[1] + 1
    spiral[row][col] = begin
    begin += 1

    # loop for down
    for i in range(1, level+1):
        row += 1
        spiral[row][col] = begin
        begin += 1

    # loop for left
    for i in range(1, level+1):
        col -= 1
        spiral[row][col] = begin
        begin += 1

    # return end point after making moves
    end_pt = [row, col]
    return end_pt

# movement of case of even level
def even(spiral, start_pt, level):
    begin = (level ** 2) + 1 # next number

    # move 1 to left
    row = start_pt[0]
    col = start_pt[1] - 1
    spiral[row][col] = begin
    begin += 1

    # loop for up
    for i in range(1, level+1):
        row -= 1
        spiral[row][col] = begin
        begin += 1

    # loop for right
    for i in range(1, level+1):
        col += 1
        spiral[row][col] = begin
        begin += 1

    # return end point after making moves
    end_pt = [row, col]
    return end_pt


# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers (spiral, n):
    top = True
    bottom = True
    sum = 0

    #Matching input
    for i in range(len(spiral)):
        for j in range(len(spiral)):
            if n == spiral[i][j]:
                #checking top
                if i-1 >= 0:
                    sum += spiral[i-1][j]
                else:
                    top = False

                #checking bot
                if i+1 <= len(spiral)-1:
                    sum += spiral[i+1][j]
                else:
                    bottom = False

                #checking left
                if j-1 >= 0:
                    sum += spiral[i][j-1]
                    if top == True:
                        sum += spiral[i-1][j-1]
                    if bottom == True:
                        sum += spiral[i+1][j-1]

                #checking right
                if j+1 <= len(spiral)-1:
                    sum += spiral[i][j+1]
                    if top == True:
                        sum += spiral[i-1][j+1]
                    if bottom == True:
                        sum += spiral[i+1][j+1]
    return sum


def main():
    # read the input file
    n = int(sys.stdin.readline())

    # create the spiral
    spiral = create_spiral(n)

    for line in sys.stdin:
        num = int(line.strip())

        # add the adjacent numbers
        result = sum_adjacent_numbers(spiral, num)

        # print the result
        print(result)

if __name__ == "__main__":
  main()