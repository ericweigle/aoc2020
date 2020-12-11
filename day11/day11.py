#!/usr/bin/python3

import re
import sys
import math
import pprint
import copy

for filename in sys.argv[1:]:
  data = [x.strip() for x in open(filename, 'r').readlines()]
  for i in range(len(data)):
    data[i] = [data[i][j] for j in range(len(data[i]))]
  #pprint.pprint(data)

  HEIGHT = len(data)
  WIDTH = len(data[0])

  def adjacencies_pt1(x,y,query):
    count = 0
    for i in (x-1,x,x+1):
      for j in (y-1,y,y+1):
        try:
          if (i==x and j==y) or i<0 or j<0 or i>=HEIGHT or j>=WIDTH:
            continue
          if data[i][j] == query:
            count += 1
        except IndexError:
          pass
    return count

  def adjacencies_pt2(x,y,query):
    count = 0

    for d_i, d_j in [(-1, -1), (0, -1), (1, -1),
                     (-1,  0),          (1,  0),
                     (-1,  1), (0,  1), (1,  1)]:
      i = x
      j = y
      while True:
        i += d_i
        j += d_j
        if i<0 or j<0 or i>=HEIGHT or j>=WIDTH:
          break
        if data[i][j] == 'L':
          break
        if data[i][j] == '#':
          count += 1
          break
    return count

  def automata(data):
    new_data = copy.deepcopy(data)
    for x in range(len(data)):
      for y in range(len(data[0])):
        ## If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
        if data[x][y]=='L':
          if adjacencies_pt2(x,y,'#')==0:
            new_data[x][y]='#'
        ## If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
  
        elif data[x][y]=='#':
          if  adjacencies_pt2(x,y,'#')>=5: # 4 for part 1
            new_data[x][y]='L'
        ## Otherwise, the seat's state does not change.
    return new_data


  def total(data, query):
    retval = 0
    for row in data:
      retval += sum([1 for x in row if x==query])
    return retval

  while True:
    new_data = automata(data)
    #pprint.pprint(automata(data))
    #print("\n")
    if new_data == data:
      break
    data = new_data

  print(total(data, '#'))
