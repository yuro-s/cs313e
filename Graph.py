#  File: Graph.py

#  Description: Complete various methods pertaining to graph modification and graph traversal.

#  Date Created: 4/28/2021

#  Date Last Modified: 4/28/2021

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

  # get edge weight between two vertices
  # return -1 if edge does not exist
  def get_edge_weight (self, fromVertexLabel, toVertexLabel):
    # convert labels to indexes
    start = self.get_index(fromVertexLabel)
    finish = self.get_index(toVertexLabel)
    # if there is no edge return -1
    if self.adjMat[start][finish] == 0:
      return -1 
    else:
      # else return weight between fromVertex to ToVertex
      return self.adjMat[start][finish]

    # get a list of immediate neighbors that you can go to from a vertex
  # return a list of indices or an empty list if there are none
  def get_neighbors (self, vertexLabel):
    neighbors = []
    # convert vertex label to an index
    vertex = self.get_index(vertexLabel)
    # iterate through all columns on the same row as vertex
    for i in range(len(self.Vertices)):
      # if weight is not 0 then it means there is a direct edge
      if self.adjMat[vertex][i] != 0:
        # add vertex to neighbor list 
        neighbors.append(self.Vertices[i])
    return neighbors

  # return an unvisited vertex adjacent to vertex v (index)
  def get_adj_unvisited_vertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
        return i
    return -1

  # get a copy of the list of Vertex objects
  def get_vertices (self):
    # return list of vertices
    return self.Vertices

  # do a depth first search in a graph
  def dfs (self, v):
    # create the Stack
    theStack = Stack ()

    # mark the vertex v as visited and push it on the Stack
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theStack.push (v)

    # visit all the other vertices according to depth
    while (not theStack.is_empty()):
      # get an adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex (theStack.peek())
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push (u)

    # the stack is empty, let us rest the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  # do the breadth first search in a graph
  def bfs (self, v):
    # create queue
    theQueue = Queue()
    # append starting node to Queue and set to visited
    self.Vertices[v].visited = True
    theQueue.enqueue(v)
    # print starting node
    print (self.Vertices[v])

    # keep going until queue is empty
    while(not theQueue.is_empty()):
      # get the vertex at the start of the queue
      top_node = theQueue.dequeue()
      # iterate through its neighbors and add direct neighbors of current vertex to queue
      for i in range(len(self.Vertices)):
        u = self.get_adj_unvisited_vertex(top_node)
        # if u is -1, means there is no more neighbors that have not been visited
        if u == -1:
          break
        else:
          # else set the neighbor to visited 
          self.Vertices[u].visited = True
          print(self.Vertices[u])
          # add neighbor to queue
          theQueue.enqueue(u)

  # delete an edge from the adjacency matrix
  # delete a single edge if the graph is directed
  # delete two edges if the graph is undirected
  def delete_edge (self, fromVertexLabel, toVertexLabel):
    # get start index
    start = self.get_index(fromVertexLabel)
    # get end index
    finish = self.get_index(toVertexLabel)
    # insert zero to express no connection
    self.adjMat[start][finish] = 0
    self.adjMat[finish][start] = 0
  
  # delete a vertex from the vertex list and all edges from and
  # to it in the adjacency matrix
  def delete_vertex (self, vertexLabel):
    vertex = self.get_index(vertexLabel)
    # delete vertex from the list of vertices
    self.Vertices.pop(vertex)
    # delete vertex from the adjMatrix
    self.adjMat.pop(vertex)
    # delete each connections
    for i in range(len(self.adjMat)):
      self.adjMat[i].pop(vertex)


def main():
  # create the Graph object
  cities = Graph()

  # read the number of vertices
  line = sys.stdin.readline()
  line = line.strip()
  num_vertices = int (line)

  # read the vertices to the list of Vertices
  for i in range (num_vertices):
    line = sys.stdin.readline()
    city = line.strip()
    cities.add_vertex (city)

  # read the number of edges
  line = sys.stdin.readline()
  line = line.strip()
  num_edges = int (line)

  # read each edge and place it in the adjacency matrix
  for i in range (num_edges):
    line = sys.stdin.readline()
    edge = line.strip()
    edge = edge.split()
    start = int (edge[0])
    finish = int (edge[1])
    weight = int (edge[2])

    cities.add_directed_edge (start, finish, weight)

  # read the starting vertex for dfs and bfs
  line = sys.stdin.readline()
  start_vertex = line.strip()

  # get the index of the starting vertex
  start_index = cities.get_index (start_vertex)

  # do the depth first search
  print ("Depth First Search")
  cities.dfs (start_index)
  print ()
  
  # do the breadth first search
  print("Breadth First Search")
  cities.bfs (start_index)
  print ()

  # read in from vertex and to vertex to delete an edge
  line = sys.stdin.readline().strip()
  line = line.split()
  
  # delete edge between cities
  cities.delete_edge(line[0], line[1])
  print("Deletion of an edge")
  print()
  print("Adjacency Matrix")
  
  # print formatted adjacency matrix
  for row in cities.adjMat:
    matrix = ' '.join(map(str, row))
    print(matrix)

  # read in vertex to be deleted
  line = sys.stdin.readline()
  vertex = line.strip()
  print()
  
  # delete vertex from list and adjacency matrix
  cities.delete_vertex(vertex)
  print("Deletion of a vertex")
  print()
  print("List of Vertices")

  # cities after delete vertex
  for i in cities.Vertices:
    print(i)
  print()
  
  # adjacency matrix after delete vertex
  print("Adjacency Matrix")
  for row in cities.adjMat:
    matrix = ' '.join(map(str, row))
    print(matrix)

if __name__ == "__main__":
  main()
