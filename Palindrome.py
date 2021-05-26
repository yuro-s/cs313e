#  File: Palindrome.py

#  Description: Create shortest palindromic string

#  Student Name: Samuel Lee

#  Student UT EID: STL467

#  Partner Name: Yuro Sato

#  Partner UT EID: ys9434

#  Course Name: CS 313E

#  Unique Number: 52240

#  Date Created: 2/28/2021

#  Date Last Modified: 2/28/2021

import sys

# Input: a lowercase string with no digits, punctuation marks, or spaces
# Output: a string that is the smallest palindrome that can be 
#         made by adding characters to the start of the input string
def smallest_palindrome(str):
  
  reverse_str = str[::-1]
  # keeps track of index of original string
  index_original = 0
  for i in range(len(str)):
    # if character is equal in both original and reversed string
    if(reverse_str[i] == str[index_original]):
      # if characters are same increment index of original string
      index_original += 1
  # if original string is already a palindrome
  if index_original == len(str):
    return str
  # check if palindrome is at beginning
  if str[0:index_original-1] == reverse_str[(len(str) - index_original):len(str) - 1]:
    # taking remainder part of the string and attach to beggining of original string
    remainder = reverse_str[0:len(str) - index_original]
    palindrome_str = remainder + str
    return palindrome_str
  else:
    # if the beginning is not a palindrome, append the whole original string reversed minus the last character
    reverse_orig = str[len(str)-1:0:-1]
    # append reversed string to beginning of original string
    palindrome_str = reverse_orig + str
    return palindrome_str
  
def main():

  for line in sys.stdin:
      # read the data
      str = line.strip()
      # print the smallest palindromic string that can be made for each input
      print(smallest_palindrome(str))

if __name__ == "__main__":
  main()
