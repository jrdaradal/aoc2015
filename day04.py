# 2015 Advent of Code Day 04 Solution
# John Roy Daradal

import hashlib
from utils import * 

# SolutionA: 254575
# SolutionB: 1038736

def input04(full: bool) -> list[str]:
    return readLines(getPath(4, full))

def day04A():
    full = True
    for key in input04(full):
        findMin(key, 5)

def day04B():
    full = True 
    for key in input04(full):
        findMin(key, 6)

def findMin(key: str, numZeros: int):
    goal = '0' * numZeros
    i = 0 
    while True:
        i += 1
        fkey = '%s%d' % (key, i)
        hash = hashlib.md5(fkey.encode('utf-8')).hexdigest()
        if hash[:numZeros] == goal:
            print(i)
            break

if __name__ == '__main__':
    day04A()
    day04B()