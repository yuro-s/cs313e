#  File: Josephus.py

#  Description: 

#  Student Name: Samuel Lee

#  Student UT EID: stl467

#  Partner Name: Yuro Sato

#  Partner UT EID:ys9434

#  Course Name: CS 313E

#  Unique Number:52230

#  Date Created:4/10/2021

#  Date Last Modified:4/10/2021

import sys

class Link(object):
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class CircularList(object):
  # Constructor
    def __init__ ( self ):
        self.first = None 

  # Insert an element (value) in the list
    def insert ( self, data ):
        new_node = Link(data)
        current = self.first
        if current == None:
            self.first = new_node
            new_node.next = self.first
        else:
            while current.next != self.first:
                current = current.next
            current.next = new_node
            new_node.next = self.first
        return

  # Find the Link with the given data (value)
  # or return None if the data is not there
    def find ( self, data ):
        current = self.first
        if current == None:
            return None
        elif current.data == data:
            return current
        else:
            current = current.next
            while current != self.first:
                if current.data == data:
                    return current
                else:
                    current = current.next
        return None
        
  # Delete a Link with a given data (value) and return the Link
  # or return None if the data is not there
    def delete ( self, data ):
        # current = self.first
        # if current == None:
        #     return None
        # elif current.data == data:
        #     return current
        # else:
        #     current = current.next
        #     while current != self.first:
        #         if current.data == data:
        #             return current
        #         else:
        #             current = current.next
        return
        
  # Delete the nth Link starting from the Link start 
  # Return the data of the deleted Link 
  # AND return the next Link for the deleted Link
    def delete_after ( self, start, n ):
        # current = self.first
        # if current == None:
        #     return None
        # else:
        return
        
  # Return a string representation of a Circular List
  # The format of the string will be the same as the __str__ 
  # format for normal Python lists
    def __str__ ( self ):
        current = self.first
        string = "["   
        if current == None:
            return string + ']'
        else:
            string = string + str(current.data) + ","
            current = current.next
            while current != self.first:
                string = string + " " + str(current.data) + ","
                current = current.next
        string = string[:-1]
        string = string + "]"
        return string

def main():
    # # read number of soldiers
    # line = sys.stdin.readline()
    # line = line.strip()
    # num_soldiers = int (line)

    # # read the starting number
    # line = sys.stdin.readline()
    # line = line.strip()
    # start_count = int (line)

    # # read the elimination number
    # line = sys.stdin.readline()
    # line = line.strip()
    # elim_num = int (line)
    
    test = CircularList()
    test.insert(1)
    test.insert(2)
    test.insert(3)
    test.insert(4)

    test.find(4)

    print(test)

  # your code

if __name__ == "__main__":
  main()