#  File: BST_Cipher.py

#  Description: Encryption and Decryption using BST

#  Date Created: 4/18/2021

#  Date Last Modified: 4/18/2021

import sys

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__ (self, encrypt_str):
        self.root = None
        for char in encrypt_str:
            self.insert(char)
        return

    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert (self, ch):
        new_node = Node (ch)
        # create node
        if self.root == None:
            self.root = new_node
            return
        else:
            current = self.root
            while current != None:
                # skip if character duplicates 
                if ch == current.data:
                    return
                # if character value less, create left node
                elif ch < current.data:
                    if current.lchild == None:
                        current.lchild = new_node
                    current = current.lchild
                # if character value greater, create right node
                else:
                    if current.rchild == None:
                        current.rchild = new_node
                    current = current.rchild

    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search (self, ch):
        string = ""
        if ch == self.root.data:
            return "*"
        current = self.root
        while current != None:
            # if char is found, return the series of special characters
            if current.data == ch:
                return string
            # if char is less than current.data append a < and go left
            elif ch < current.data:
                string = string + "<"
                current = current.lchild
            # if char is greater than current.data append a > and go right
            elif ch > current.data:
                string = string + ">"
                current = current.rchild
        # if char is not found, return empty string
        return ""

    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding 
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse (self, st):
        if len(st) == 0:
            return ""
        current = self.root
        for i in range(len(st)):
            # if current reaches end, then no valid character in tree
            if current == None:
                return ""
            if st[i] == "*":
                return self.root.data
            # traverse left if character is <
            elif st[i] == "<":
                current = current.lchild
            # traverse right if character is >
            else:
                current = current.rchild

        return current.data

    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt (self, st):
        # convert string to lowercase
        st.lower()
        string = ""
        # iterate through string to find series of unique characters
        for char in st:
            string = string + self.search(char) + "!"
        # remove last exclamation mark
        string = string[:-1] 
        return string

    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt (self, st):
        string = ""
        decrypt_st = ""
        if len(st) == 0:
            return ""
        # iterate through decrypted string to find a string
        for i in range(len(st)):
            # last character
            if i == len(st)-1:
                string += st[i]
                decrypt_st += self.traverse(string)
            # determine every character from series of unique characters 
            if st[i] == "!":
                decrypt_st += self.traverse(string)
                string = "" 
            # append unique characters to empty string
            else:
                string += st[i]
        return decrypt_st


    # def printTree(self, aNode):
    #     if(aNode != None):
    #         self.printTree(aNode.lchild)
    #         print(aNode.data)
    #         self.printTree(aNode.rchild)
            
def main():
    # read encrypt string
    line = sys.stdin.readline()
    encrypt_str = line.strip()

    # create a Tree object
    the_tree = Tree (encrypt_str)

    # read string to be encrypted
    line = sys.stdin.readline()
    str_to_encode = line.strip()

    # # print the encryption
    print (the_tree.encrypt(str_to_encode))

    # read the string to be decrypted
    line = sys.stdin.readline()
    str_to_decode = line.strip()

    # # print the decryption
    print (the_tree.decrypt(str_to_decode))
 
if __name__ == "__main__":
  main()
