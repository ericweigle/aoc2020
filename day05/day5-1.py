#!/usr/bin/python3

import re
import sys
import math

def get_row(value):
  low = 0
  high = 127

  for choice in value:
    #print(choice)
    assert choice in ('F', 'B')
    middle = (low + high) / 2
    #print(low, middle, high)
    if choice == 'F':
      high = int(math.floor(middle))
    else: # == 'B':
      low = int(math.ceil(middle))

    #print("   ", choice, low, high)
  assert low == high
  return low

# Brandon's binary solution(s)
def get_row_fast(value):
  return int(value.replace('F','0').replace('B','1'),2)

def get_col_fast(value):
  return int(value.replace('L','0').replace('R','1'),2)

def get_col(value):
  low = 0
  high = 7

  for choice in value:
    #print(choice)
    assert choice in ('L', 'R')
    middle = (low + high) / 2
    #print(low, middle, high)
    if choice == 'L':
      high = int(math.floor(middle))
    else: # == 'R':
      low = int(math.ceil(middle))

    #print("   ", choice, low, high)
  assert low == high
  return low


# Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".
# 
# The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.
# 
# For example, consider just the first seven characters of FBFBBFFRLR:
# 
# Start by considering the whole range, rows 0 through 127.
# F means to take the lower half, keeping rows 0 through 63.
# B means to take the upper half, keeping rows 32 through 63.
# F means to take the lower half, keeping rows 32 through 47.
# B means to take the upper half, keeping rows 40 through 47.
# B keeps rows 44 through 47.
# F keeps rows 44 through 45.
# The final F keeps the lower of the two, row 44.


def get_seat_id(row, col): 
  return get_row(row) * 8 + get_col(col)

assert get_row('FBFBBFF') == 44
assert get_col('RLR')==5
assert get_seat_id('FBFBBFF', 'RLR')==357

#print(get_seat_id("BFFFBBF", "RRR")) # : row 70, column 7, seat ID 567.
#print(get_seat_id("FFFBBBF", "RRR")) # : row 14, column 7, seat ID 119.
#print(get_seat_id("BBFFBBF", "RLL")) # : row 102, column 4, seat ID 820

#sys.exit(1)
for filename in sys.argv[1:]:
  print("For %s" % filename)
  data = [x.strip() for x in open(filename, 'r').readlines()]
  for seat in data:
    row, col = seat.split(" ")
    assert get_row(row) == get_row_fast(row)
    assert get_col(col) == get_col_fast(col)
    print(get_seat_id(row,col))
    #jrow = get_row(row)
    #col = get_col(col)


# The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.


# 
# For example, consider just the last 3 characters of FBFBBFFRLR:
# 
# Start by considering the whole range, columns 0 through 7.
# R means to take the upper half, keeping columns 4 through 7.
# L means to take the lower half, keeping columns 4 through 5.
# The final R keeps the upper of the two, column 5.
# So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.
# 
# Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.
# 
# Here are some other boarding passes:
# 
# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.
# As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?
# 
# To begin, get your puzzle input.
# 
# ANSWER 963
#Ding! The "fasten seat belt" signs have turned on. Time to find your seat.
#
#It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.
#
#Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.
#
#What is the ID of your seat?
#
#Answer: 
#   
#
#   Although it hasn't changed, you can still get your puzzle input.
#
#   You can also [Share] this puzzle.
