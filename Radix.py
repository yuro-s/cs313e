
#  File: Radix.py

#  Description: Sort list of strings containing lower case letter and numbers 
#               0-9 using modified Radix Sort.

#  Date Created: 4/3/2021

#  Date Last Modified: 4/3/2021

import sys

class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue if empty
  def is_empty (self):
    return (len(self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len(self.queue))

# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):
  letter_dict = {}
  queue_list = []
  # populate dictionary with indexes of numbers 0-9
  for i in range(0,10):
    letter_dict[str(i)] = str(i)
  next_idx = 10
  # populate dictionary with indexes of lower case letters
  for i in range(97, 123):
    letter_dict[chr(i)] = str(next_idx)
    next_idx += 1
  # create list of queues
  for i in range(len(letter_dict)):
    queue = Queue()
    queue_list.append(queue)

  # get max length of string in word list
  max_length = len(max(a, key = len))
  # append asterisks to strings to help with uneven string length
  for i in range(len(a)):
    diff = max_length - len(a[i])
    if diff != 0:
      for k in range(diff):
        temp = a[i].split()
        # add '*' to merge string size
        temp.append('*')
        a[i] = ''.join(temp)

  # modified Radix sorting algorithm 
  for i in range(1, max_length+1):
    for word in a:
        item = word[-i]
        # if character is '*' add to queue 0
        if item == "*":
          queue_list[0].enqueue(word)
          continue
        # put string in appropriate queue number based on
        # dictionary value
        value = letter_dict[item]
        # enqueue word in queue
        queue_list[int(value)].enqueue(word)
    # list to append sorted elments
    a = []
    # dequeue elements in queue list for next iteration
    for queue in queue_list:
      while queue.size() != 0:
        a.append(queue.dequeue())
        
  # delete all asteriks from strings
  for i in range(len(a)):
    for char in a[i]:
      if char == '*':
        a[i] = a[i].replace(char, '')
  
  return a


def main():
  # read the number of words in file
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int (line)

  # create a word list
  word_list = []
  for i in range (num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append (word)

  '''
  # print word_list
  print (word_list)
  '''

  # use radix sort to sort the word_list
  sorted_list = radix_sort (word_list)

  # print the sorted_list
  print (sorted_list)

if __name__ == "__main__":
  main()

    
