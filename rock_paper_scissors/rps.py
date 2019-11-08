#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  def recursion_rps(possibilities):
    updated_possibilities = []
    for start in [['rock'], ['paper'], ['scissors']]:
      for rest in possibilities:
        updated_possibilities.append(start+rest)
    return updated_possibilities
  
  if n == 0:
    return [[]]
  possibilities = [['rock'], ['paper'], ['scissors']]
  while n > 1:
    possibilities = recursion_rps(possibilities)
    n -= 1
  return possibilities



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')