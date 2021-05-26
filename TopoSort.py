#  File: TopoSort.py

#  Description: Create method checking if graph has a cycle and perform a topological sort on graph.

#  Student Name: Samuel Lee

#  Student UT EID: stl467

#  Partner Name: Yuro Sato

#  Partner UT EID: ys9434

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 5/2/2021

#  Date Last Modified: 5/2/2021

import sys

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek (self):
    return self.stack[-1]

  # check if the stack if empty
  def is_empty (self):
    return (len (self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len (self.stack))


class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue is empty
  def is_empty (self):
    return (len (self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len (self.queue))


class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def was_visited (self):
    return self.visited

  # determine the label of the vertex
  def get_label (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)


class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # get a list of Vertex object labels
  def get_vertices (self):
    list_letters = []
    for vertex in self.Vertices:
      list_letters.append(vertex.get_label())
    return list_letters

  # check if a vertex is already in the graph
  def has_vertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return True
    return False

  # given the label get the index of a vertex
  def get_index (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def add_vertex (self, label):
    if (self.has_vertex (label)):
      return

    # add vertex to the list of vertices
    self.Vertices.append (Vertex (label))

    # add a new column in the adjacency matrix
    nVert = len (self.Vertices)
    for i in range (nVert - 1):
      (self.adjMat[i]).append (0)

    # add a new row for the new vertex
    new_row = []
    for i in range (nVert):
      new_row.append (0)
    self.adjMat.append (new_row)

  # add weighted directed edge to graph
  def add_directed_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def add_undirected_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to vertex v (index)
  def get_adj_unvisited_vertex_dfs (self, v, stack):
    nVert = len (self.Vertices)
    for i in range (nVert):
      # if the vertex is already in the stack that means there is a cycle
      if self.adjMat[v][i] > 0:
        if i in stack:
          return -10
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
        return i
    return -1

  # determine if a directed graph has a cycle
  # this function should return a boolean and not print the result
  def has_cycle (self):
    # need to perform a DFS for each vertex to check for cycle in directed graph
    for v in range(len(self.Vertices)):
    # create the Stack
      theStack = Stack()
    
    # mark the vertex v as visited and push it on the Stack
      (self.Vertices[v]).visited = True
      theStack.push (v)
    # visit all the other vertices according to depth
      while (not theStack.is_empty()):
        # get an adjacent unvisited vertex
        u = self.get_adj_unvisited_vertex_dfs(theStack.peek(), theStack.stack)
        # if u is equal to -10 that means there is a cycle, return True
        if u == -10:
          return True
        elif (u == -1):
          u = theStack.pop()
        else:
          (self.Vertices[u]).visited = True
          theStack.push (u)

    # the stack is empty, let us rest the flags
      nVert = len (self.Vertices)
      for i in range (nVert):
        (self.Vertices[i]).visited = False
        
    # indicates there is no cycle
    return False

  # return a list of vertices after a topological sort
  # this function should not print the list
  
  def toposort (self):
    # create list contains availble nodes
    available_nodes = []
    for i in range(len(self.Vertices)):
      available_nodes.append(i)
    # create list of sorted nodes
    theQueue = []
    
    # iterate through list of available nodes
    while len(available_nodes) > 0:
      # create list of nodes with in_degrees of zero
      in_degree_zero = []
      temp = []
      # append value of in degree to temp list
      for i in available_nodes:
        temp.append(self.in_degree(i))
      # iterate through temp
      for i in temp:
        # if in degree is zero, append to in_degree_zero list
        if i[1] == 0:
          in_degree_zero.append(i[0])
      # iterates through in_degree_zero list
      for i in in_degree_zero:
        # remove nodes with in degrees of zero from available_nodes
        available_nodes.remove(i)
        # append nodes with in degrees of zero to list
        theQueue.append(self.get_vertices()[i])
        # delete edge from adjacent matrix by converting them into zero
        for j in range(len(self.Vertices)):
          if self.adjMat[i][j] == 1:
            self.adjMat[i][j] = 0

    return theQueue

  # calculates the number of degrees going into a vertex
  def in_degree (self, index):
    # creates a list with index of vertex in adjMat and the in degree
    in_degree_list = [index,]
    # calculates the sum of all indegrees
    in_degree_sum = 0
    # goes through all entries of matrix from top to bottom
    for i in range(len(self.Vertices)):
      if self.adjMat[i][index] == 1:
        in_degree_sum += 1
    
    in_degree_list.append(in_degree_sum)
    return in_degree_list

def main():

  # create a Graph object
  theGraph = Graph()
  # read the number of vertices
  line = sys.stdin.readline()
  line = line.strip()
  num_vertices = int (line)

  # read the vertices to the list of Vertices
  for i in range (num_vertices):
    line = sys.stdin.readline()
    vertex = line.strip()
    theGraph.add_vertex (vertex)

  # print(theGraph.get_vertices())
  # read the number of edges
  line = sys.stdin.readline()
  line = line.strip()
  num_edges = int (line)

  # read each edge and place it in the adjacency matrix
  for i in range (num_edges):
    line = sys.stdin.readline()
    edge = line.strip()
    edge = edge.split()
    start = int(theGraph.get_vertices().index(edge[0]))
    finish = int(theGraph.get_vertices().index(edge[1]))
    theGraph.add_directed_edge (start, finish)

  # test if a directed graph has a cycle
  if (theGraph.has_cycle()):
    print ("The Graph has a cycle.")
  else:
    print ("The Graph does not have a cycle.")

  # test topological sort
  if (not theGraph.has_cycle()):
    vertex_list = theGraph.toposort()
    print ("\nList of vertices after toposort")
    print (vertex_list)
    
main()
