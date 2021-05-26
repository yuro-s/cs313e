#  File: Cipher.py

#  Description: Encrypting and Decrypting given string input

#  Student Name: Samuel Lee

#  Student UT EID: STL467

#  Partner Name: Yuro Sato

#  Partner UT EID: YS9434

#  Course Name: CS 313E

#  Unique Number: 52240

#  Date Created: 2/6/2021

#  Date Last Modified: 2/6/2021

import math
import sys
# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def encrypt(strng):

    # Number asterisk
    asterisk = math.ceil(math.sqrt(len(strng))) ** 2 - len(strng)

    # adding asterisk to input string
    strng_asterisk = strng + ('*' * asterisk)

    matrix = []

    # creating 2D matrix
    for i in range(math.ceil(math.sqrt(len(strng)))):
        line = []
        for element in range(0, math.ceil(math.sqrt(len(strng)))):
            line.append(0)
        matrix.append(line)

    row = 0
    col = math.ceil(math.sqrt(len(strng))) - 1

    # iterating through the string and encrypting
    for num in strng_asterisk:
        matrix[row][col] = num
        row += 1
        if (row > math.ceil(math.sqrt(len(strng))) - 1 ):
            row = 0
            col -=1

    temp_strng = ''
    strng = ''

    # joining all the characters on each line
    for i in range(len(matrix)):
        temp_strng = temp_strng.join(matrix[i])
        strng += temp_strng
        temp_strng = ''

    # taking out asterisks in string
    strng = (strng.replace('*', ''))

    return strng

def decrypt (strng):

    asteriks = math.ceil(math.sqrt(len(strng)))**2 - len(strng)
    
    matrix = []
    
    for i in range(0, math.ceil(math.sqrt(len(strng)))):
        line = []
        for element in range(0, math.ceil(math.sqrt(len(strng)))):
            line.append(0)
        matrix.append(line)

    row = math.ceil(math.sqrt(len(strng)))-1
    col = 0

    for num in range(0, asteriks):
        matrix[row][col] = "*"
        row = row - 1
        if(row < 0):
            row = math.ceil(math.sqrt(len(strng)))-1
            col = col + 1

    index = 0

    for line in range (0, math.ceil(math.sqrt(len(strng)))):
        for element in range (0, math.ceil(math.sqrt(len(strng)))):
            if (matrix[line][element] == "*"):
                continue
            matrix[line][element] = strng[index]
            index = index + 1

    strng = ""
    column = math.ceil(math.sqrt(len(strng)))-1

    for line in matrix:
        row = 0
        for element in line:
            element = matrix[row][column]
            if element != "*":
                strng = strng + element 
            row = row + 1
        column = column - 1
        
    return strng

def main():
    #read the two strings P and Q from standard imput
    input_encrypt = sys.stdin.readline().strip()
    input_decrypt = sys.stdin.readline().strip()

    # encrypt the string P
    encrypt(input_encrypt)
    # decrypt the string Q
    decrypt(input_decrypt)

    # print the encrypted string of P and the
    print(encrypt(input_encrypt))
    # decrypted string of Q to standard out
    print(decrypt(input_decrypt))

if __name__ == "__main__":
    main()