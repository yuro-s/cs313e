
#  File: Triangle.py

#  Description: Find the greatest path sum

#  Student Name: Yuro Sato

#  Student UT EID: ys9434

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created:3/29/2021

#  Date Last Modified:3/29/2021

import sys

from timeit import timeit

# returns the greatest path sum using exhaustive search
def brute_force (grid):
  idx1 = 0
  idx2 = 0
  path = []
  sum = 0
  brute_force_helper(grid, idx1, idx2, path, sum)
  return max(path)

def brute_force_helper(grid,idx1, idx2, path, sum):
  # base case if it reached the bottom of triangle
  if idx1 >= (len(grid)):
    path.append(sum)
    return
  else:
    sum += grid[idx1][idx2]
  # take bottom left value or bottom right
  return brute_force_helper(grid,idx1+1, idx2, path, sum) or brute_force_helper(grid, idx1+1, idx2+1, path, sum)

# returns the greatest path sum using greedy approach
def greedy (grid):
  start_idx = 1
  end_idx = 0
  return grid[0][0] + greedy_helper(grid, start_idx, end_idx)

# helper function of greedy to use recursion
def greedy_helper (grid, start_idx, end_idx):
  # base case if it reached the bottom of triangle
  if start_idx >= len(grid):
    return 0
  else:
    # take value if the next one is bigger
    if grid[start_idx][end_idx] > grid[start_idx][end_idx+1]:
      return grid[start_idx][end_idx] + greedy_helper(grid,start_idx+1,end_idx)
    # take value if the current one is bigger
    else:
      return grid[start_idx][end_idx+1] + greedy_helper(grid,start_idx+1,end_idx+1)

# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer(grid):
  start_idx = 0
  end_idx = 0
  sum = 0
  return max(divide_conquer_helper(grid, start_idx, end_idx, sum))

# helper function divide_conquer to use recursion
def divide_conquer_helper(grid, start_idx, end_idx, sum):
  # base case if it reached the bottom of the triangle
  if start_idx >= len(grid):
    return [sum]
  else:
    if start_idx == len(grid) - 1:
      return divide_conquer_helper(grid, start_idx + 1, end_idx, sum + grid[start_idx][end_idx])
    else:
      return divide_conquer_helper(grid, start_idx + 1, end_idx, sum + grid[start_idx][end_idx]) + \
      divide_conquer_helper(grid, start_idx + 1, end_idx + 1, sum + grid[start_idx][end_idx])

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog(grid):
  start_idx = 0
  end_idx = 0
  return dynamic_prog_helper(grid, start_idx, end_idx)

# helper function of dynamic_prog to use recursion
def dynamic_prog_helper(grid, start_idx, end_idx):
  # base case if it reached the bottom of the triangle
  if start_idx >= len(grid):
    return 0
  else:
    a = grid[start_idx][end_idx] + dynamic_prog_helper(grid, start_idx + 1, end_idx)
    b = grid[start_idx][end_idx] + dynamic_prog_helper(grid, start_idx + 1, end_idx + 1)
    return max(a,b)

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # read number of lines
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty grid with 0's
  grid = [[0 for i in range (n)] for j in range (n)]

  # read each line in the input file and add to the grid
  for i in range (n):
    line = sys.stdin.readline()
    line = line.strip()
    row = line.split()
    row = list (map (int, row))
    for j in range (len(row)):
      grid[i][j] = grid[i][j] + row[j]

  return grid 

def main ():
  # read triangular grid from file
  grid = read_file()
  
  '''
  # check that the grid was read in properly
  print (grid)
  '''

  # output greatest path from exhaustive search
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  # print time taken using exhaustive search
  print("The greatest path sum through exhaustive search is")
  print(brute_force(grid))
  print("The time taken for exhaustive search in second is")
  print(times)
  print()
  # output greatest path from greedy approach
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  # print time taken using greedy approach
  print("The greatest path sum through greedy search is")
  print(greedy(grid))
  print("The time taken for greedy search in second is")
  print(times)
  print()
  # output greatest path from divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  # print time taken using divide-and-conquer approach
  print("The greatest path sum through recursive search is")
  print(divide_conquer(grid))
  print("The time taken for recursive search in second is")
  print(times)
  print()
  # output greatest path from dynamic programming 
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  # print time taken using dynamic programming
  print("The greatest path sum through dynamic programming is")
  print(dynamic_prog(grid))
  print("The time taken for dynamic programming in second is")
  print(times)
  print()
if __name__ == "__main__":
  main()

