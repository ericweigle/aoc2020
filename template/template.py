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
    pass
  else:
    # real
    pass
