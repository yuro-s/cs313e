#  File: OfficeSpace.py

#  Description: Program will output total office space, unallocated office space,
#               contested office space, and the uncontested cubicle space
#               for each individual employee, based on the requested cubicle and 
#               office parameters.

#  Date Created: 2/13/2021

#  Date Last Modified: 2/14/2021

import sys

# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area (rect):
  dif_x = rect[2] - rect[0]
  dif_y = rect[3] - rect[1]
  area =  dif_x * dif_y
  return area 

# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap
def overlap (rect1, rect2):
  # checks to see if either rectangle is on the left that is not overlapping
  if ((rect1[2] < rect2[0]) or (rect1[0] > rect2[2])):
    return (0,0,0,0)
  # checks to see if either rectangle is on the top that is not overlapping
  if((rect1[3] < rect2[1]) or (rect1[1] > rect2[3])):
    return (0,0,0,0)
  # computes the overlapping rectangle 
  x1 = max(rect1[0], rect2[0])
  y1 = max(rect1[1], rect2[1])
  x2 = min(rect1[2], rect2[2])
  y2 = min(rect1[3], rect2[3])
  return (x1, y1, x2, y2)
    
# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated 
#         space in the office
def unallocated_space (bldg):
  # finds all 0s in 2d matrix and adds them up
  num_empty_spaces = 0
  for row in bldg:        
    for col in row:
      if col == 0:
        num_empty_spaces += 1
  return num_empty_spaces

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested 
#         space in the office
def contested_space (bldg):
  # finds all spaces with a number greater than 1 in 2d matrix
  num_contested_spaces = 0
  for row in bldg:
    for col in row:
      if col > 1:
        num_contested_spaces += 1
  return num_contested_spaces

# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested 
#         space in the office that the employee gets
def uncontested_space (bldg, rect):
  num_uncontested_spaces = 0
  # sets starting coordinate
  top_left_x = rect[0]
  top_left_y = rect[1]
  # goes through the area bounded by the rect coordinates
  for k in range(rect[2]-rect[0]):
    for j in range(rect[3]-rect[1]):
      if bldg[top_left_x][top_left_y] == 1:
        # increments if space is 1, indicating uncontested space
        num_uncontested_spaces += 1
      top_left_y += 1
    top_left_x += 1
    top_left_y = rect[1]
  return num_uncontested_spaces
  
# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):
  # makes entire office space and populates with 0
  bldg = []
  for i in range(office[0]):
    row = []
    for k in range(office[1]):
      row.append(0)
    bldg.append(row)

  # populate office with occupied cubicles
  for i in range(len(cubicles)):
    # starting coordinate of requested cubicle space
    top_left_x = cubicles[i][0]
    top_left_y = cubicles[i][1]
    # loops through the area bounded by rect coordinate
    for k in range((cubicles[i][2]-cubicles[i][0])):
      for j in range((cubicles[i][3]-cubicles[i][1])):
        # add 1 for every space encountered in area bounded by rect coordinates
        bldg[top_left_x][top_left_y] = bldg[top_left_x][top_left_y] + 1
        # increment column on same row
        top_left_y += 1
      # increment row
      top_left_x += 1
      # reset column when there is a new row
      top_left_y = cubicles[i][1]
      
  return bldg

# Input: no input
# Output: a string denoting all test cases have passed
# def test_cases ():
#   return "all test cases passed"

def main():
  # read office size
  office = sys.stdin.readline().strip().split()
  cubicles = []
  names = []

  # get number of individuals
  num = int(sys.stdin.readline().strip())

  # read each employees' name and requested cubicle coordinates
  for i in range(num):
    coordinates = sys.stdin.readline().strip().split()
    names.append(coordinates[0])
    coordinates = (int(coordinates[1]), int(coordinates[2]), int(coordinates[3]), int(coordinates[4]))
    cubicles.append(coordinates)

  # get 2d matrix of office
  bldg = request_space((int(office[0]), int(office[1])), cubicles)

  # print the following results after computation
  # compute the total office space
  print('Total', int(office[0]) * int(office[1]))
  # compute the total unallocated space
  print('Unallocated',unallocated_space(bldg))
  # compute the total contested space
  print('Contested', contested_space(bldg))
  # compute the uncontested space that each employee gets
  for i in range(len(cubicles)):
    print(names[i], uncontested_space(bldg,cubicles[i]))

if __name__ == "__main__":
  main()
