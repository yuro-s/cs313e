#  File: Geometry.py

#  Description: Multiple classes contains geometrical formulas

#  Date Created: 2/6/2021

#  Date Last Modified:

import math
import sys

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0):
    self.x = x
    self.y = y
    self.z = z

  # create a string representation of a Point
  # returns a string of the form (x, y, z)
  def __str__ (self):
    return '('+ str(self.x) + ', ' + str(self.y) + str(self.z) + ')'
  
  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
  def distance (self, other):
    return math.hypot(self.x - other.x, self.y - other.y, self.z - other.z)
    
  # test for equality between two points
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
    tol = 1.0e-6
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol) and (abs(self.z - other.z) < tol))

class Sphere (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
    self.radius = radius
    self.center = Point(x,y,z)
      
  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
  def __str__ (self):
    return 'Cneter: '+ str(self.center) + ', Radius:' + str(self.radius)
  # compute surface area of Sphere
  # returns a floating point number
  def area (self):
    return 4 * math.pi * (self.radius ** 2)
  
  # compute volume of a Sphere
  # returns a floating point number
  def volume (self):
    return (4 / 3) * math.pi * (self.radius ** 3) 
    
  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
  def is_inside_point (self, p):
    return self.center.distance(p) < self.radius

  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, other):
    dist_centers = self.center.distance(other.center)
    return (dist_centers + other.radius) < self.radius

  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    dist = self.center.distance(a_cube.center)
    return (dist + (math.hypot(a_cube.side,a_cube.side))/2) <= self.radius

  # deterine if a Cylinder is strictly inside this Sphere
  #   # a_cyl is a Cylinder objectm
  # returns a Boolean
  def is_inside_cyl (self, a_cyl):
    dist = self.center.distance(a_cyl.center)
    return (dist + a_cyl.radius) < self.radius and (abs(self.center.z - a_cyl.center.z) + a_cyl.height/2.0) < self.radius

  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean
  def does_intersect_sphere (self, other):
    dist = self.center.distance(other.center)
    return dist < (self.radius + other.radius)

  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, a_cube):
    dist = self.center.distance(a_cube.center)
    hypot = math.hypot(a_cube.side,a_cube.side)
    if (self.radius + hypot/2) <= dist and (self.radius + hypot/2) >= dist:
      return True
    else:
      return False

  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
  def circumscribe_cube (self):
    return (2 * self.radius) / math.sqrt(3)

class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0, y = 0, z = 0, side = 1):
    self.side = side
    self.center = Point(x, y, z)

  # string representation of a Cube of the form:
  # Center: (x, y, z), Side: value
  def __str__ (self):
    return 'Center: ' + '(' + str(self.center.x) + ', ' + str(self.center.y) +', '+ str(self.center.z) + ')' + \
           'Side:' + str(self.side)

  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
  def area (self):
    return 6 * (self.side **2)

  # compute volume of a Cube
  # returns a floating point number
  def volume (self):
    return self.side ** 3

  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def is_inside_point (self, p):
    dist = p.distance(self.center)
    return self.side/2 > dist

  # determine if a Sphere is strictly inside this Cube
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    dist = self.center.distance(a_sphere.center)
    return (dist + a_sphere.radius) < (self.side/2)

  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_inside_cube (self, other):
    dist = self.center.distance(other.center)
    return (dist + other.side) < self.side

  # determine if a Cylinder is strictly inside this Cube
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, a_cyl):
    return a_cyl.height < self.side

  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, other):
    dist = self.center.distance(other.center)
    return  dist < (self.side + other.side)

  # determine the volume of intersection if this Cube
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
  def intersection_volume (self, other):
    x_intersection = min(self.center.x + self.side/2, other.center.x + other.side/2) \
                     - max(self.center.x - self.side/2, other.center.x - other.side/2)
    y_intersection = min(self.center.y + self.side/2, other.center.y + other.side/2) \
                     - max(self.center.y - self.side/2, other.center.y - other.side/2)
    z_intersection = min(self.center.z + self.side/2, other.center.z + other.side/2) \
                     - max(self.center.z - self.side/2, other.center.z - other.side/2)
    return x_intersection * y_intersection * z_intersection

  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
  def inscribe_sphere (self):
    diagonal_xy = math.hypot(self.side, self.side)
    diagonal_xyz = math.hypot(diagonal_xy, self.side)
    radius = diagonal_xyz/2
    return Sphere(self.center.x, self.center.y, self.center.z, radius)

class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
    self.radius = radius
    self.height = height
    self.center = Point(x, y, z)

  # returns a string representation of a Cylinder of the form:
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
    return 'Center: ' + '(' + str(self.center.x) + ', ' + str(self.center.y) +', '+ str(self.center.z) + ')'\
           ', Radius: ' + str(self.radius) + ', Height: ' + str(self.height)
  # compute surface area of Cylinder
  # returns a floating point number
  def area (self):
    return (2 * math.pi * self.radius * self.height) + (2 * math.pi * self.radius**2)

  # compute volume of a Cylinder
  # returns a floating point number
  def volume (self):
    return math.pi * self.radius**2 * self.height

  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  def is_inside_point (self, p):
    dist_xz = math.hypot(abs(self.center.x - p.x), \
                         abs(self.center.z - p.z))
    dist_y = abs(self.center.y - p.y)
    return (self.radius > dist_xz) and (self.height/2 > dist_y)

  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    dist_xz = math.hypot(abs(self.center.x - p.x), \
                         abs(self.center.z - p.z))
    dist_y = abs(self.center.y - p.y)
    return (self.radius > (a_sphere.radius + dist_xz)) and (self.height > (a_sphere.height/2 + dist_y))

  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    dist_xz = math.hypot(abs(self.center.x - p.x), \
                         abs(self.center.z - p.z))
    dist_y = abs(self.center.y - p.y)
    cube_xy = math.hypot(a_cube.side, a_cube.side)
    return self.radius > cube_xy/2 + dist_xz and self.height > a_cube.side + dist_y

  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, other):
    dist_xz = math.hypot(abs(self.center.x - other.center.x), \
                         abs(self.center.z - other.center.z))
    dist_y = abs(self.center.y - p.y)
    return self.radius > (other.radius + dist_xz) \
           and self.height > (other.height + dist_y)

  # determine if another Cylinder intersects this Cylinder
  # two Cylinder object intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cylinder object
  # returns a Boolean
  def does_intersect_cylinder (self, other):
    dist_xz = math.hypot(abs(self.center.x - other.center.x),\
                         abs(self.center.z - other.center.z))
    return (dist_xz < (abs(self.radius - other.radius))) \
           and (abs(self.center.y - other.center.y) < abs((self.height - other.height)))

def main():
  # read data from standard input
  
  # read the coordinates of the first Point p
  input_p = (sys.stdin.readline().strip().split(' '))
  # create a Point object
  p = Point(float(input_p[0]), float(input_p[1]), float(input_p[2]))
  # read the coordinates of the second Point q
  input_q = (sys.stdin.readline().strip().split(' '))
  # create a Point object
  q = Point(float(input_q[0]), float(input_q[1]), float(input_q[2]))
  # read the coordinates of the center and radius of sphereA
  input_sphereA = (sys.stdin.readline().strip().split(' '))
  # create a Sphere object
  sphereA = Sphere(float(input_sphereA[0]), float(input_sphereA[1]), float(input_sphereA[2]), float(input_sphereA[3]))
  print(sphereA.radius)
  # read the coordinates of the center and radius of sphereB
  input_sphereB = (sys.stdin.readline().strip().split(' '))
  # create a Sphere object
  sphereB = Sphere(float(input_sphereB[0]), float(input_sphereB[1]), float(input_sphereB[2]), float(input_sphereB[3]))
  # read the coordinates of the center and side of cubeA
  input_cubeA = (sys.stdin.readline().strip().split(' '))
  # create a Cube object
  cubeA = Cube(float(input_cubeA[0]), float(input_cubeA[1]), float(input_cubeA[2]), float(input_cubeA[3]))
  # read the coordinates of the center and side of cubeB
  input_cubeB = (sys.stdin.readline().strip().split(' '))
  # create a Cube object
  cubeB = Cube(float(input_cubeB[0]), float(input_cubeB[1]), float(input_cubeB[2]), float(input_cubeB[3]))
  # read the coordinates of the center, radius and height of cylA
  input_cylA = (sys.stdin.readline().strip().split(' '))
  # create a Cylinder object
  cylA = Cylinder(float(input_cylA[0]), float(input_cylA[1]), float(input_cylA[2]), float(input_cylA[3]))
  # read the coordinates of the center, radius and height of cylB
  input_cylB = (sys.stdin.readline().strip().split(' '))
  # create a Cylinder object
  cylB = Cylinder(float(input_cylB[0]), float(input_cylB[1]), float(input_cylB[2]), float(input_cylB[3]))

  # print if the distance of p from the origin is greater
  # than the distance of q from the origin
  origin = Point()
  if p.distance(origin) > q.distance(origin):
    print("Distance of Point p from the origin is greater than the distance of Point q from the origin")
  else:
    print("Distance of Point p from the origin is not greater than the distance of Point q from the origin")
  # print if Point p is inside sphereA
  if sphereA.is_inside_point(p) == True:
    print("Point p is inside sphereA")
  else:
    print("Point p is not inside sphereA")

  # print if sphereB is inside sphereA
  if sphereA.is_inside_sphere(sphereB) == True:
    print("sphereB is inside sphereA")
  else:
    print("sphereB is not inside sphereA")

  # print if cubeA is inside sphereA
  if sphereA.is_inside_cube(cubeA) == True:
    print("cubeA is inside sphereA")
  else:
    print("cubeA is not inside sphereA")

  # print if cylA is inside sphereA
  if sphereA.is_inside_cyl(cylA) == True:
    print("cylA is inside sphereA")
  else:
    print("cylA is not inside sphereA")

  # print if sphereA intersects with sphereB
  if sphereB.does_intersect_sphere(sphereA) == True:
    print("sphereA does intersect sphereB")
  else:
    print("sphereA is not inside sphereB")

  # print if cubeB intersects with sphereB
  if sphereB.does_intersect_cube(cubeB) == True:
    print("cubeB does intersect sphereB")
  else:
    print("cubeB does intersect sphereB")

  # print if the volume of the largest Cube that is circumscribed
  # by sphereA is greater than the volume of cylA
  if (sphereA.circumscribe_cube() ** 3) > cylA.volume():
    print("Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA")
  else:
    print("Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA")

  # print if Point p is inside cubeA
  if cubeA.is_inside_point(p) == True:
    print("Point p is inside cubeA")
  else:
    print("Point p is not inside cubeA")

  # print if sphereA is inside cubeA
  if cubeA.is_inside_sphere(sphereA) == True:
    print("sphereA is inside cubeA")
  else:
    print("sphereA is not inside cubeA")

  # print if cubeB is inside cubeA
  if cubeA.is_inside_cube(cubeB) == True:
    print("cubeB is inside cubeA")
  else:
    print("cubeB is not inside cubeA")

  # print if cylA is inside cubeA
  if cubeA.is_inside_cylinder(cylA) == True:
    print("cylA is inside cubeA")
  else:
    print("cylA is not inside cubeA")

  # print if cubeA intersects with cubeB
  if cubeA.does_intersect_cube(cubeB) == True:
    print("cubeA does intersect cubeB")
  else:
    print("cubeA does not intersect cubeB")

  # print if the intersection volume of cubeA and cubeB
  # is greater than the volume of sphereA
  if cubeA.intersection_volume(cubeB) > sphereA.volume():
    print("Intersection volume of cubeA and cubeB is greater than the volume of sphereA")
  else:
    print("Intersection volume of cubeA and cubeB is not greater than the volume of sphereA")

  # print if the surface area of the largest Sphere object inscribed
  # by cubeA is greater than the surface area of cylA
  if cubeA.inscribe_sphere().area() > cylA.area():
    print("Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA")
  else:
    print("Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA")

  # print if Point p is inside cylA
  if cylA.is_inside_point(p) == True:
    print("Point p is inside cylA")
  else:
    print("Point p is not inside cylA")
  # print if sphereA is inside cylA
  if cylA.is_inside_sphere(sphereA) == True:
    print("sphereA is inside cylA")
  else:
    print("sphereA is not inside cylA")
  # print if cubeA is inside cylA
  if cylA.is_inside_cube(cubeA) == True:
    print("cubeA is inside cylA")
  else:
    print("cubeA is not inside cylA")

  # print if cylB is inside cylA
  if cylA.is_inside_cylinder(cylB) == True:
    print("cylB is inside cylA")
  else:
    print("cylB is not inside cylA")

  # print if cylB intersects with cylA
  if cylA.does_intersect_cylinder(cylB) == True:
    print("cylA does intersect cylB")
  else:
    print("cylA does not intersect cylB")

if __name__ == "__main__":
  main()
