
#  File: Hull.py

#  Description: Find the vertices of the smallest convex polygon that encloses a set of points.
#               Print out area of convex hull using determinant. 

#  Student Name: Samuel Lee

#  Student UT EID: stl467

#  Partner Name: Yuro Sato

#  Partner UT EID: ys9434

#  Course Name: CS313E

#  Unique Number: 52240

#  Date Created: 2/15/2021

#  Date Last Modified: 2/15/2021

import sys
import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):
  matrix = [[1, p.x, p.y], [1, q.x, q.y], [1, r.x, r.y]]
  # Equation of 3x3 determinant
  det = ((matrix[0][0])*((matrix[1][1]*matrix[2][2])-(matrix[1][2]*matrix[2][1])))-\
        ((matrix[0][1])*((matrix[1][0]*matrix[2][2])-(matrix[1][2]*matrix[2][0]))) +\
          ((matrix[0][2]*((matrix[1][0]*matrix[2][1])-(matrix[1][1]*matrix[2][0]))))
  return det

# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull (sorted_points):
  # create empty list upper hull
  upper_hull = []
  # append first 2 points in sorted_points to upper_hull
  upper_hull.append(sorted_points[0])
  upper_hull.append(sorted_points[1])
  for i in range (2, len(sorted_points)):
    last_three_det = 1
    upper_hull.append(sorted_points[i])
    # check right and left 
    while((len(upper_hull) >= 3) and last_three_det > 0):
      last_three_det = det(upper_hull[-3], upper_hull[-2], upper_hull[-1])
      # if determinant is positive, delete middle point of last three points
      if last_three_det > 0:
        del upper_hull[-2]

  # create empty list lower hull
  sorted_points.reverse()
  lower_hull = []
  # append last 2 points in reversed_point_list
  lower_hull.append(sorted_points[0])
  lower_hull.append(sorted_points[1])
  for i in range(2, len(sorted_points)):
    last_three_det_low = 1
    lower_hull.append(sorted_points[i])
    # check right and left
    while((len(lower_hull) >= 3) and last_three_det_low > 0):
      last_three_det_low = det(lower_hull[-3], lower_hull[-2], lower_hull[-1])
      # if determinant is positive, delete middle point of last three points
      if last_three_det_low > 0:
        del lower_hull[-2]
  # delete duplicates between lower and upper hall lists
  del lower_hull[0]
  del lower_hull[-1]
  # add lower hull list to upper hull list
  upper_hull.extend(lower_hull)
  return upper_hull 

# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):
  det = 0
  # add all determinant up to (xn-1,yn-1)
  for i in range(len(convex_poly)):
    if i == (len(convex_poly)-1):
      break
    else:
      # equation of 2x2 matrix determinant
      det += (convex_poly[i].x * convex_poly[i+1].y) - (convex_poly[i].y * convex_poly[i+1].x)
  # det of (x1,y1) and (xn,yn)
  det += (convex_poly[len(convex_poly)-1].x * convex_poly[0].y) - (convex_poly[len(convex_poly)-1].y * convex_poly[0].x)
  # get the area of polygon
  area = (0.5) * abs(det)

  return area

# Input: no input
# Output: a string denoting all test cases have passed
# def test_cases():
#   return "all test cases passed"

def main():
  #create an empty list of Point objects
  points_list = []
  # read number of points
  line = sys.stdin.readline()
  line = line.strip()
  num_points = int (line)

  # read data from standard input
  for i in range (num_points):
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    x = int (line[0])
    y = int (line[1])
    points_list.append (Point (x, y))
    
  # # sort the list according to x-coordinates
  sorted_points = sorted (points_list)

  # #print the sorted list of Point objects
  # for p in sorted_points:
  #   print (str(p))

  # get the convex hull
  convex = convex_hull(sorted_points)

  # print your results to standard output
  # print the convex hull
  print('Convex Hull')
  for i in range(len(convex)):
    print(convex[i])
  print()
  # get the area of the convex hull
  area = area_poly(convex)
  
  # print the area of the convex hull
  print("Area of Convex Hull =", area)
if __name__ == "__main__":
  main()   