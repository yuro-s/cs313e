#  File: Boxes.py

#  Description: Generate all subsets of boxes and find a largest subset and it's frequency

#  Date Created: 3/25/2021

#  Date Last Modified: 3/25/2021

import sys

# generates all subsets of boxes and stores them in all_box_subsets
# box_list is a list of boxes that have already been sorted
# sub_set is a list that is the current subset of boxes
# idx is an index in the list box_list
# all_box_subsets is a 3-D list that has all the subset of boxes
def sub_sets_boxes (box_list, sub_set, idx, all_box_subsets):
    # end recursion when index reaches end of list
    if idx == len(box_list):
        all_box_subsets.append(sub_set)
        return
    else:
        original = sub_set[:]
        sub_set.append(box_list[idx])
        # append element to sub_set and increment index by 1
        sub_sets_boxes(box_list, sub_set, idx+1, all_box_subsets)
        # keep sub_set the same and increment index by 1
        sub_sets_boxes(box_list, original, idx+1, all_box_subsets)

# goes through all the subset of boxes and only stores the
# largest subsets that nest in the 3-D list all_nesting_boxes
# largest_size keeps track what the largest subset is
def largest_nesting_subsets (all_box_subsets):
  nest_list = []
 # Take single subset 
  for boxes in all_box_subsets:
    if len(boxes) == 0:
      continue
    start_idx = 0
    end_idx = 1
    sub_sets = [boxes[0],]
    # recursive helper to help create subset of boxes that fit inside each other
    largest_nesting_subsets_helper(start_idx, end_idx, nest_list, sub_sets, boxes)

  # Find the largest subset size
  largest_size = 0 
  for i in nest_list:
    if len(i) > largest_size:
      largest_size = len(i)
    
  # Find the frequency of largest subset  
  count = 0 
  for i in nest_list:  
    if len(i) == largest_size:
      count += 1

  return largest_size, count

def largest_nesting_subsets_helper(start_idx, end_idx, nest_list, sub_sets, boxes):
  # base case is if end_idx reached to the end
  if end_idx >= len(boxes):
    # check to see if sub_set is already in nest_list to avoid duplicates
    if sub_sets in nest_list:
      return
    else:
      nest_list.append(sub_sets)
      return
  # if boxes fit inside each other, append box to sub_sets list
  if does_fit(boxes[start_idx], boxes[end_idx]):
    sub_sets.append(boxes[end_idx])
    start_idx = end_idx
    # recurse with new sub_sets list and increment index by 1
    largest_nesting_subsets_helper(start_idx, end_idx+1, nest_list, sub_sets, boxes)
  else:
    # recurse with no change to sub_sets list and increment index by 1
    largest_nesting_subsets_helper(start_idx, end_idx+1, nest_list, sub_sets, boxes)
      
# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
    # read the number of boxes 
    line = sys.stdin.readline()
    line = line.strip()
    num_boxes = int (line)

    # create an empty list for the boxes
    box_list = []

    # read the boxes from the file
    for i in range (num_boxes):
      line = sys.stdin.readline()
      line = line.strip()
      box = line.split()
      for j in range (len(box)):
          box[j] = int (box[j])
      box.sort()
      box_list.append (box)

    '''
    # print to make sure that the input was read in correctly
    print (box_list)
    print()
    '''

    # sort the box list
    box_list.sort()

    '''
    # print the box_list to see if it has been sorted.
    print (box_list)
    print()
    '''

    # create an empty list to hold all subset of boxes
    all_box_subsets = []

    # create a list to hold a single subset of boxes
    sub_set = []
    # generate all subsets of boxes and store them in all_box_subsets
    sub_sets_boxes (box_list, sub_set, 0, all_box_subsets)
    # all_box_subsets should have a length of 2^n where n is the number
    # of boxes

    # go through all the subset of boxes and only store the
    # largest subsets that nest in all_nesting_boxes
    all_nesting_boxes = largest_nesting_subsets (all_box_subsets)

    # print the largest number of boxes that fit

    print(all_nesting_boxes[0])

    # print the number of sets of such boxes

    print(all_nesting_boxes[1])

if __name__ == "__main__":
  main()
