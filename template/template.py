#!/usr/bin/python3

import re
import sys
import math
import pprint
import copy

for filename in sys.argv[1:]:
  data = [int(x.strip()) for x in open(filename, 'r').readlines()]

  if len(data) < 100:
    # example
  else:
    # real

  target = get_target(preamble, data)
  get_target2(target, data)
