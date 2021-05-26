#  File: OfficeSpace.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:

# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area (rect):

# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap
def overlap (rect1, rect2):

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated
#         space in the office
def unallocated_space (bldg):

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested
#         space in the office
def contested_space (bldg):

# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested
#         space in the office that the employee gets
def uncontested_space (bldg, rect):

# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
  assert area ((0, 0, 1, 1)) == 1
  # write your own test cases

  return "all test cases passed"

def main():
  # read the data

  # run your test cases
  '''
  print (test_cases())
  '''

  # print the following results after computation

  # compute the total office space

  # compute the total unallocated space

  # compute the total contested space

  # compute the uncontested space that each employee gets

if __name__ == "__main__":
  main()