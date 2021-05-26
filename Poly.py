#  File: Poly.py

#  Description: Creating a polynomial

#  Student Name: Yuro Sato

#  Student UT EID: ys9434

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 4/16/2021

#  Date Last Modified: 4/16/2021

import sys

class Link (object):
    def __init__ (self, coeff = 1, exp = 1, next = None):
        self.coeff = coeff
        self.exp = exp
        self.next = next

    def __str__ (self):
        return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
    def __init__ (self):
        self.first = None

  # keep Links in descending order of exponents
    def insert_in_order (self, coeff, exp):
        new_node = Link(coeff, exp)
        current = self.first

        # create first node
        if self.first == None:
            new_node.next = self.first
            self.first = new_node
        # insert bigger exponent in the list
        elif self.first.exp <= new_node.exp:
            new_node.next = self.first
            self.first = new_node
        # insert smaller exponents in the list
        else:
            while current.next != None and current.next.exp > new_node.exp:
                current = current.next
            new_node.next = current.next
            current.next = new_node


    # add polynomial p to this polynomial and return the sum
    def add (self, p):
        sum_list = LinkedList()
        current = self.first
        p_current = p.first

        # case p is empty
        if self.first == None:
            return p
        # case q is empty
        elif p.first == None:
            return self
        else:
            while current != None and p_current != None:
                # add coefficients when exponents are same
                if current.exp == p_current.exp:
                    sum_list.insert_in_order((current.coeff + p_current.coeff), current.exp)
                    current = current.next
                    p_current = p_current.next
                # case p has greater exponent
                elif current.exp > p_current.exp:
                    sum_list.insert_in_order(current.coeff, current.exp)
                    current = current.next
                # case q has greater exponent
                else:
                    sum_list.insert_in_order(p_current.coeff, p_current.exp)
                    p_current = p_current.next
            # insert rest of the node of p
            while current != None:
                sum_list.insert_in_order(current.coeff, current.exp)
                current = current.next
            # insert rest of the node of q
            while p_current != None:
                sum_list.insert_in_order(p_current.coeff, p_current.exp)
                p_current = p_current.next
            return sum_list

    # multiply polynomial p to this polynomial and return the product
    def mult (self, p):
        product_list = LinkedList()
        current = self.first
        p_current = p.first

        # case p is empty
        if self.first == None:
            return p
        # case q is empty
        elif p.first == None:
            return self
        else:
            # multiply node of p by node of q
            while current != None:
                while p_current != None:
                    product_list.insert_in_order((current.coeff * p_current.coeff), (current.exp + p_current.exp))
                    p_current = p_current.next
                current = current.next
                p_current = p.first
        return product_list

    # simplifies the polynomial
    def arth_helper(self):
        current = self.first
        temp = current.next
        # take current node
        while current != None:
            # add nodes with same exponent
            while temp != None and temp.exp == current.exp:
                current.coeff += temp.coeff
                current.next = temp.next
                temp = temp.next
            current = current.next
            if current != None:
                temp = current.next

    # create a string representation of the polynomial
    def __str__ (self):
        current = self.first
        string = '('
        if current == None:
            return
        else:
            while current != None:
                if current.coeff == 0:
                    current = current.next
                else:
                    string = string + str(current.coeff) + ', ' + str(current.exp) + ') + ('
                    current = current.next
        string = string[:-4]
        return string

def main():

  # create polynomial p
    p = LinkedList()
    n = sys.stdin.readline()
    n = n.strip()
    num_lines = int(n)
    for i in range(num_lines):
        line = sys.stdin.readline()
        line = line.strip()
        line = line.split()
        p.insert_in_order(int(line[0]), int(line[1]))
    sys.stdin.readline()

  # create polynomial q
    q = LinkedList()
    n = sys.stdin.readline()
    n = n.strip()
    num_lines = int(n)
    for i in range(num_lines):
        line = sys.stdin.readline()
        line = line.strip()
        line = line.split()
        q.insert_in_order(int(line[0]), int(line[1]))

  # get sum of p and q and print sum
    add = p.add(q)
    add.arth_helper()
    print(add)

  # get product of p and q and print product
    product = p.mult(q)
    product.arth_helper()
    print(product)

if __name__ == "__main__":
  main()