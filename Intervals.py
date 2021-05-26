#  File: Intervals.py

#  Description: Merge and sort intervals

#  Student Name: Samuel Lee

#  Student UT EID: STL467

#  Partner Name: Yuro Sato

#  Partner UT EID: YS9434

#  Course Name: CS 313E

#  Unique Number: 52240

#  Date Created: 2/2/2021

#  Date Last Modified: 2/2/2021

import sys

# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval
def merge_tuples (tuples_list):

    interval_list = []
    tuples_list.sort(key = lambda x: x[0])
    interval_list.append(tuples_list[0])
    ptr_interval = 0
    # merge intervals
    for i in range(1, len(tuples_list)):
        insert_tup = ['','']
        if tuples_list[i][0] <= interval_list[ptr_interval][1]:
            insert_tup[0] = interval_list[ptr_interval][0]
            if tuples_list[i][1] >= interval_list[ptr_interval][1]:
                insert_tup[1] = tuples_list[i][1]
            else:
                insert_tup[1] = interval_list[ptr_interval][1]
            interval_list[ptr_interval] = insert_tup
        else:
            interval_list.append(tuples_list[i])
            ptr_interval += 1

    # converting from lists to tuples
    for i in range(len(interval_list)):
        convert = tuple(interval_list[i])
        interval_list[i] = convert

    return interval_list

# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval
def sort_by_interval_size (tuples_list):
    interval_dif = []
    # Relating interval and size of it by 2D list
    for i in range(0, len(tuples_list)):
        temp_list = []
        temp_list.append(tuples_list[i])
        temp_list.append(abs(tuples_list[i][0] - tuples_list[i][1]))
        interval_dif.append(temp_list)

    interval_dif.sort(key=lambda x: x[1])
    interval_dif = same_interval(interval_dif)

    return interval_dif

# sorts same size of interval by lower end
def same_interval(tuples_list):
    final_list = []
    temp_list = []
    temp_list.append(tuples_list[0][0])
    temp_size = tuples_list[0][1]

    # sorting the intervals of same size
    for i in range(1, len(tuples_list)):
        if temp_size == tuples_list[i][1]:
            temp_list.append(tuples_list[i][0])
        else:
            temp_list.sort(key=lambda x: x[0])
            final_list.extend(temp_list)
            temp_list.clear()
            temp_list.append(tuples_list[i][0])
            temp_size = tuples_list[i][1]

    temp_list.sort(key=lambda x: x[0])
    final_list.extend(temp_list)
    return final_list

# Input: no input
# Output: a string denoting all test cases have passed
# def test_cases ():
#   assert merge_tuples([(1,2)]) == [(1,2)]
#   # write your own test cases

#   assert sort_by_interval_size([(1,3), (4,5)]) == [(4,5), (1,3)]
#   # write your own test cases

#   return "all test cases passed"

def main():
    tuples_list = []
  # open file intervals.in and read the data and create a list of tuples
    input = int(sys.stdin.readline())
    for line in sys.stdin:
        # tuples_list = (line.strip(' '))
        test = line.strip()
        test = test.split(' ')
        test[0] = int(test[0])
        test[1] = int(test[1])
        insert_tup = tuple(test)
        tuples_list.append(insert_tup)

  # merge the list of tuples
    merge_list = merge_tuples(tuples_list)
  # sort the list of tuples according to the size of the interval
    sort_list = sort_by_interval_size(merge_list)

  # run your test cases

  # write the output list of tuples from the two functions
    print(merge_list)
    print(sort_list)
if __name__ == "__main__":
  main()