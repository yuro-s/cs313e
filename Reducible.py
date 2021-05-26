#  File: Reducible.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name: Yuro Sato

#  Partner UT EID: ys9434

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 3/30/2021

#  Date Last Modified: 3/30/2021

import sys

# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
  if (n == 1):
    return False

  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True

# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word (s, size):
  hash_idx = 0
  for j in range (len(s)):
    letter = ord (s[j]) - 96
    hash_idx = (hash_idx * 26 + letter) % size
  return hash_idx

# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size (s, const):
  return const - hash_word(s,const)

# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing

def insert_word (s, hash_table):
  idx = hash_word(s, len(hash_table))
  if hash_table[idx] == '':
    hash_table[idx] = s
    return
  else:
    i = 0
    idx2 = step_size(s,5)
    dh = (idx + i*idx2) % len(hash_table)
    while hash_table[dh] != '': 
      i +=1
      dh = (idx + i*idx2) % len(hash_table)
    hash_table[dh] = s
  return

# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word (s, hash_table):
  idx = hash_word(s, len(hash_table))
  if hash_table[idx] == s:
    return True
  else:
    i = 0
    idx2 = step_size(s,5)
    dh = (idx + i*idx2) % len(hash_table)
    while hash_table[dh] != '':                
      if hash_table[dh] == s:
        return True
      i +=1
      dh = (idx + i*idx2) % len(hash_table)
    return False

# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):
  if find_word(s, hash_memo) == True:
    return True

  if len(s) == 1:
    if s == 'a' or s =='i' or s == 'o':
      return True
    else:
      return False

  for i in range(len(s)):
    new_string = s[:i] + s[i+1:]
    if new_string == 'a' or new_string =='i' or new_string == 'o':
      loop = 0
    else:
        if find_word(new_string, hash_table) == False:
          continue
    if is_reducible(new_string, hash_table, hash_memo) == True:
        insert_word(new_string, hash_memo)
        return True

  return False

# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):
  list_max = []
  max_length = max(string_list, key = len)
  for i in string_list:
    if len(i) == len(max_length):
      list_max.append(i)
      
  return list_max

def get_list_len(factor,list_length):
  length = factor*list_length
  while(is_prime(length) == False):
    length += 1
  return length

def main():
  # create an empty word_list
  word_list = []

  # read words from words.txt and append to word_list
  for line in sys.stdin:
    line = line.strip()
    word_list.append (line)

  # find length of word_list

  list_length = len(word_list)

  # determine prime number N that is greater than twice
  # the length of the word_list

  hash_list_len = get_list_len(2,list_length)

  # create an empty hash_list

  hash_list = []

  # populate the hash_list with N blank strings

  for i in range(hash_list_len):
    hash_list.append('')

  # hash each word in word_list into hash_list
  # for collisions use double hashing 

  for word in word_list:
    insert_word (word, hash_list)

  # create an empty hash_memo of size M
  hash_memo = []
  # we do not know a priori how many words will be reducible
  # let us assume it is 10 percent (fairly safe) of the words
  # then M is a prime number that is slightly greater than 
  # 0.2 * size of word_list
  m = int(get_list_len(0.2, list_length))

  # populate the hash_memo with M blank strings
  # for i in range(m):
  for i in range(m):
    hash_memo.append('')

  # create an empty list reducible_words
  reducible_words = []

  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
  # as you recursively remove one letter at a time check
  # first if the sub-word exists in the hash_memo. if it does
  # then the word is reducible and you do not have to test
  # any further. add the word to the hash_memo.

  for i in range(len(word_list)):
    if is_reducible(word_list[i], hash_list, hash_memo) == True:
      reducible_words.append(word_list[i])

  # find the largest reducible words in reducible_words
  # print the reducible words in alphabetical order
  # one word per line

  for i in get_longest_words(reducible_words):
    print(i)

if __name__ == "__main__":
  main()