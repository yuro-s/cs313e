#  File: ExpressionTree.py

#  Description: Create expression and evaluate expression.
#               Print out pre-order and post-order expressions.

#  Date Created: 4/17/2021

#  Date Last Modified: 4/18/2021

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = None
    
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        if self.root == None:
            new_node = Node()
            self.root = new_node
        tree_stack = Stack()
        current = self.root
        expr = expr.split()
        # iterate through expression to create tree
        for i in expr:
            # if left parenthesis, create new left node 
            if i == '(':
                new_node = Node()
                current.lChild = new_node
                tree_stack.push(current)
                current = current.lChild
            # if operators, set current operator to a current node and create right node
            elif i in operators:
                new_node = Node()
                current.data = i
                tree_stack.push(current)
                current.rChild = new_node
                current = current.rChild
            # if right parenthesis, make current node equal to parent node
            elif i == ')':
                if not tree_stack.is_empty():
                    current = tree_stack.pop()
            # if operand, set current operand to a current node
            else:
                current.data = i
                current = tree_stack.pop()
        return

    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        # terminating condition is if node has no child, return data
        if aNode.lChild == None and aNode.rChild == None:
            return aNode.data
        # traverse down left side
        left = self.evaluate(aNode.lChild)
        # traverse down right side
        right = self.evaluate(aNode.rChild)
        # evaluate expression
        expression = str(left) + aNode.data + str(right)
        return float(eval(expression))
        
    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        expression = []
        # call helper function to generate list of nodes traversed
        self.pre_order_helper(aNode, expression)
        # join list containing expression
        string_exp = ' '.join(expression)
        return string_exp
    
    def pre_order_helper(self, aNode, expression):
        if(aNode != None):
            # append data to expression list
            expression.append(aNode.data)
            # traverse left side
            self.pre_order_helper(aNode.lChild, expression)
            # traverse right side
            self.pre_order_helper(aNode.rChild, expression)
    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        expression = []
        # call helper function to generate list of nodes traversed
        self.post_order_helper(aNode, expression)
        # join list containing expression
        string_exp = ' '.join(expression)
        return string_exp

    def post_order_helper(self, aNode, expression):
        if(aNode != None):
            # traverse left side
            self.post_order_helper(aNode.lChild, expression)
            # traverse right side
            self.post_order_helper(aNode.rChild, expression)
            # append data to expression list
            expression.append(aNode.data)

# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
    tree = Tree()
    tree.create_tree(expr)
    # # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()
