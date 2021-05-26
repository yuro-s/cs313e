#  File: Josephus.py

#  Description: Solve the Josephus problem given a starting soldier and a count n.
#               Print executed soldiers in order.

#  Date Created:4/10/2021

#  Date Last Modified:4/11/2021

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
        # if no elements in linked list add to head
        if current == None:
            self.first = new_node
            # point node.next to first node
            new_node.next = self.first
        else:
            # else add to end of linked list and point next to first node
            while current.next != self.first:
                current = current.next
            current.next = new_node
            new_node.next = self.first
        return

  # Find the Link with the given data (value)
  # or return None if the data is not there
    def find ( self, data ):
        current = self.first
        # no value found since list is empty
        if current == None:
            return None
        # if value is first node then return first node
        elif current.data == data:
            return current
        else:
            # else traverse through linked list to find value
            current = current.next
            # traverse till you reach the first node
            while current != self.first:
                if current.data == data:
                    return current
                else:
                    current = current.next

        # if value not found after traverse, return None
        return None
        
  # Delete a Link with a given data (value) and return the Link
  # or return None if the data is not there
    def delete ( self, data ):
        current = self.first
        previous = self.first
        if current == None:
            return None
        # if deleted element is the first element and no element after
        if current.data == data and current.next == self.first:
            self.first = None
            return current
        # if deleted element is the first element and there are elements in linked list
        elif current.data == data and current.next != self.first:
            last = self.first
            current = current.next
            # traverse to end of linked list in order to reattach end node next to new first node
            while current != self.first:
                if current.next == self.first:
                    last = current
                current = current.next
            self.first = current.next
            last.next = self.first
            return current
        else:
            current = current.next
            while current != self.first:
                # if value is found, attach previous to the next node after current
                if current.data == data:
                    previous.next = current.next
                    return current
                else:
                    previous = current
                    current = current.next
        
        return None
        
  # Delete the nth Link starting from the Link start 
  # Return the data of the deleted Link 
  # AND return the next Link for the deleted Link
    def delete_after ( self, start, n ):
        # iterate n-1 times to next node to be deleted
        for i in range(n-1):
            start = start.next
        # holds the next node position of the one being deleted
        next_pt = start.next
        # return a tuple of the data of the node deleted as well as ref. to next node
        return self.delete(start.data).data, next_pt
        
  # Return a string representation of a Circular List
  # The format of the string will be the same as the __str__ 
  # format for normal Python lists
    def __str__ ( self ):
        current = self.first
        string = "["   
        # returns [] if no elements in linked list
        if current == None:
            return string + ']'
        else:
            string = string + str(current.data) + ","
            current = current.next
            # traverses array and appends value to string representation
            while current != self.first:
                string = string + " " + str(current.data) + ","
                current = current.next
        # delete last comma if last value in list
        string = string[:-1]
        string = string + "]"
        return string

def main():
    # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int (line)

    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int (line)

    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int (line)
    # create new circular linked list
    soldier_list = CircularList()
    # populate list with number of soldiers
    for i in range(1, num_soldiers+1):
        soldier_list.insert(i)
    # gets reference of the start node
    next_node = soldier_list.find(start_count)
    # keeps deleting soldiers until linked list becomes empty
    while(soldier_list.first != None):
        result_tuple = soldier_list.delete_after(next_node,elim_num)
        # prints value of soldier deleted which is first element in tuple
        print(result_tuple[0])
        # second element in tuple is the ref. to the next node of the deleted node
        next_node = result_tuple[1]

if __name__ == "__main__":
  main()
