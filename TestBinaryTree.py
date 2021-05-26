#  File: TestBinaryTree.py

#  Description: Created various function associated binary search tree.

#  Student Name: Samuel Lee

#  Student UT EID: stl467

#  Partner Name: Yuro Sato

#  Partner UT EID: ys9434

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 4/25/2021

#  Date Last Modified: 4/25/2021

import sys

class Node (object):

  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
    def __init__ (self):
      self.root = None

    # insert data into the tree
    def insert (self, data):
      new_node = Node (data)
      if (self.root == None):
        self.root = new_node
        return
      else:
        current = self.root
        parent = self.root
        while (current != None):
          parent = current
          if (data < current.data):
            current = current.lchild
          else:
            current = current.rchild

        # found location now insert node
        if (data < parent.data):
          parent.lchild = new_node
        else:
          parent.rchild = new_node
            
    # Returns true if two binary trees are similar
    def is_similar (self, pNode):
        # create two empty lists to compare
        original_list = []
        other_list = []
        self.is_similar_helper(self.root, original_list)
        self.is_similar_helper(pNode.root, other_list)

        # if they are same return true
        if original_list == other_list:
            return True
        # if they are different return false
        else:
            return False
            
    def is_similar_helper(self, pNode, node_list):
        if pNode != None:
            # append data to expression list
            node_list.append(pNode.data)
            # traverse left side
            self.is_similar_helper(pNode.lchild, node_list)
            # traverse right side
            self.is_similar_helper(pNode.rchild, node_list)
        
            
    # Returns a list of nodes at a given level from left to right
    def get_level (self, level): 
      # store nodes in the given level
      node_list = []
      aNode = self.root
      if self.root == None:
        return node_list
      else:
        # helper to append nodes in level to a list
        self.get_level_helper(aNode, level, node_list)
        return node_list

    def get_level_helper(self, aNode, level,node_list):
      # stop condition is when we get to the desired level
      if level == 0:
        node_list.append(aNode)
      else:
        # checks to see if node is the leaf node
        if aNode.lchild != None:
          # traverse left and decrease level by 1
          self.get_level_helper(aNode.lchild, level-1, node_list)
        if aNode.rchild != None:
          # traverse right and decrease level by 1
          self.get_level_helper(aNode.rchild, level-1, node_list)
        return 

    # Returns the height of the tree
    def get_height (self):
      aNode = self.root
      return self.get_height_helper(aNode)
    
    def get_height_helper(self, aNode):
      if aNode == None:
        return 0
      else:
        # when we traverse left we increase height by 1
        left = self.get_height_helper(aNode.lchild) + 1
        # when we traverse right we increase height by 1
        right = self.get_height_helper(aNode.rchild) + 1
      
        # return maximum of left and right to get largest height
        return max(left, right)

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes (self):
      aNode = self.root
      return self.num_nodes_helper(aNode)
    
    # helper functon to sum number of nodes
    def num_nodes_helper (self, aNode):
      # return 0 if node is none
      if aNode == None:
        return 0
      # sum number of nodes
      else:
        total = self.num_nodes_helper(aNode.lchild) + self.num_nodes_helper(aNode.rchild).data + 1
        return total

def main():

  # Create three trees - two are the same and the third is different
  line = sys.stdin.readline()
  line = line.strip()
  line = line.split()
  tree1_input = list (map (int, line)) 	# converts elements into ints

  tree1 = Tree()

  for i in tree1_input:
      tree1.insert(i)

  # tree1.printTree(tree1.root)

  line = sys.stdin.readline()
  line = line.strip()
  line = line.split()
  tree2_input = list (map (int, line)) 	# converts elements into ints

  tree2 = Tree()

  for i in tree2_input:
      tree2.insert(i)

  # tree2.insert(tree2.root)
  print(tree2.is_similar(tree1.root))

  line = sys.stdin.readline()
  line = line.strip()
  line = line.split()
  tree3_input = list (map (int, line)) 	# converts elements into ints

  tree3 = Tree()

  for i in tree3_input:
      tree3.insert(i)
  
  # Test your method is_similar()
  print(tree2.is_similar(tree3.root))
  # Print the various levels of two of the trees that are different
  print(tree1.get_height())
  # Get the height of the two trees that are different
  print(tree1.get_level(3))
  # Get the total number of nodes a binary search tree
  print(tree1.num_nodes())

if __name__ == "__main__":
  main()