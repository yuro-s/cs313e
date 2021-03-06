#  File: TestLinkedList.py

#  Description: Implement various methods relating to Linked Lists.

#  Date Created:4/8/2021

#  Date Last Modified:4/8/2021

class Link(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList(object):
    # create a linked list
    # you may add other attributes
    def __init__(self):
        self.first = None

    # get number of links
    def get_num_links(self):
        count = 0
        current = self.first
        while current != None:
            count +=1
            current = current.next
        return count

    # add an item at the beginning of the list
    def insert_first(self, data):
        new_node = Link(data)
        new_node.next = self.first
        self.first = new_node

    # add an item at the end of a list
    def insert_last(self, data):
        new_node = Link(data)
        current = self.first
        if current == None:
            self.first = new_node
        else:
            while current.next != None:
                current = current.next
            current.next = new_node
        return

    # add an item in an ordered list in ascending order
    # assume that the list is already sorted
    def insert_in_order(self, data):
        current = self.first
        previous = current

        if current == None or current.data >= data:
            self.insert_first(data)
        else:
            while current != None:
                if current.next == None:
                    self.insert_last(data)
                    break
                if previous.data < data and current.data > data:
                    self.insert_middle(data, previous, current)
                    break
                else:
                    previous = current
                    current = current.next
        return

    def insert_middle(self, data, previous, current):
        new_node = Link(data)
        previous.next = new_node
        new_node.next = current
        return 

    # search in an unordered list, return None if not found
    def find_unordered(self, data):
        current = self.first
        if current == None:
            return None
        else:
            while current != None:
                if current.data == data:
                    return current
                current = current.next
            return None
                    
    # Search in an ordered list, return None if not found
    def find_ordered(self, data):
        current = self.first
        if current == None:
            return None
        else:
            while current != None:
                if current.data == data:
                    return current
                current = current.next
            return None

    # Delete and return the first occurrence of a Link containing data
    # from an unordered list or None if not found
    def delete_link(self, data):
        previous = self.first
        current = self.first

        if (current == None):
            return None

        while (current.data != data):
            if (current.next == None):
                return None
            else:
                previous = current
                current = current.next

        if (current == self.first):
            self.first = self.first.next
        else:
            previous.next = current.next

        return current

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        current = self.first
        count = 0
        string = ""
        while(current != None):
            if count == 10:
                count = 0
                string = string + "\n" + str(current.data) + "  "
            else:
                string = string + str(current.data) + "  "
            count += 1
            current = current.next
        return string
        
    # Copy the contents of a list and return new list
    # do not change the original list
    def copy_list(self):
        new_linked_list = LinkedList()
        current = self.first
        if current == None:
            return new_linked_list
        else:
            while(current != None):
                new_linked_list.insert_last(current.data)
                current = current.next
        
        return new_linked_list
    # Reverse the contents of a list and return new list
    # do not change the original list
    def reverse_list(self):
        new_linked_list = LinkedList()
        current = self.first
        if current == None:
            return new_linked_list
        else:
            while current != None:
                new_linked_list.insert_first(current.data)
                current = current.next
        return new_linked_list

    # Sort the contents of a list in ascending order and return new list
    # do not change the original list
    def sort_list(self):
        new_linked_list = self.copy_list()
        flag = 0
        # Use bubble sort to sort linked list
        while(flag == 0):
            # flag will determine if no more swaps are made after a pass, exist if no more swaps
            flag = flag + 1
            current = new_linked_list.first
            previous = current
            while current.next != None:
                # if first element is bigger than second element, perform a swap
                if current.data > current.next.data:
                    # checks to see if there is a swap between first and second element in linked list
                    if new_linked_list.first == current:
                        temp = current.next
                        new_linked_list.first = temp
                        current.next = temp.next
                        temp.next = current
                        flag = 0
                    # swaps rest of linked list if needed
                    else:
                        temp = current.next
                        first = previous
                        first.next = temp
                        previous = temp
                        current.next = temp.next
                        temp.next = current
                        flag = 0
                else:
                    previous = current
                    current = current.next

        return new_linked_list


    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted(self):
        current = self.first
        previous = current
        if current == None:
            return True
        else:
            while(current != None):
                if current.data < previous.data:
                    return False
                previous = current
                current = current.next
                
        return True

    # Return True if a list is empty or False otherwise
    def is_empty(self):
        if self.first == None:
            return True
        else:
            return False
        
    # Merge two sorted lists and return new list in ascending order
    # do not change the original lists
    def merge_list(self, other):
        new_linked_list = LinkedList()
        # create two variables that start at head of each linked list
        current_self = self.first
        other_self = other.first
        # if the one of the lists is empty, return the other linked list
        if current_self == None:
            return other
        elif other_self == None:
            return self
        # keep iterating through both lists until we reach teh end of both or one of the linked lists
        while((current_self != None) and (other_self != None)):
            # if the data in linked list 1 is smller than data in linked list 2, inseert linkedlist1 data into new list
            if current_self.data < other_self.data:
                new_linked_list.insert_last(current_self.data)
                current_self = current_self.next
            else:
                # insert linkedlist 2 data into new list
                new_linked_list.insert_last(other_self.data)
                other_self = other_self.next
        # checks to see which linked list is empty if linked lists are unbalanced
        if current_self != None:
            # if linkedlist 1 is not empty, put rest of contents into new linked list
            while(current_self != None):
                new_linked_list.insert_last(current_self.data)
                current_self = current_self.next
        elif other_self != None:
            # if linkedlist 2 is not empty, put rest of contents into new linked list
            while(other_self != None):
                new_linked_list.insert_last(other_self.data)
                other_self = other_self.next

        return new_linked_list

    # Test if two lists are equal, item by item and return True
    def is_equal(self, other):
        # if both lists are empty, then they are equal
        if other.is_empty == True and self.is_empty == True:
            return True
        current_self = self.first
        other_self = other.first
        # iterate through both lists until the end is reached in either both or one list
        while((current_self != None) and (other_self != None)):
            if current_self.data != other_self.data:
                return False    
            current_self = current_self.next
            other_self = other_self.next
        # if there is still one linked list that is not empty then the linked lists are unbalanced and not equal
        if current_self != None or other_self != None:
            return False

        return True
    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    # do not change the original list
    def remove_duplicates(self):
        # first sort linked list for easy deletion later
        new_linked_list = self.copy_list()
        current = new_linked_list.first
        
        if current == None:
            return None
        else:
            # checks to see if there is the same value next to the first occurance of a value
            while current.next != None:
                if current.data == current.next.data:
                    new_linked_list.delete_link(current.data)
                    current = current.next
                else:
                   current = current.next
        return new_linked_list

    
def main():

    linked_list = LinkedList()

# print(linked_list.remove_duplicates())


# Test methods insert_first() and __str__() by adding more than
# 10 items to a list and printing it.

# Test method insert_last()

# Test method insert_in_order()

# Test method get_num_links()

# Test method find_unordered()
# Consider two cases - data is there, data is not there

# Test method find_ordered()
# Consider two cases - data is there, data is not there

# Test method delete_link()
# Consider two cases - data is there, data is not there

# Test method copy_list()

# Test method reverse_list()

# Test method sort_list()

# Test method is_sorted()
# Consider two cases - list is sorted, list is not sorted

# Test method is_empty()

# Test method merge_list()

# Test method is_equal()
# Consider two cases - lists are equal, lists are not equal

# Test remove_duplicates()

if __name__ == "__main__":
    main()
