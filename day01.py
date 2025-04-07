# 2015 Advent of Code Day 01 Solution
# John Roy Daradal 

from utils import *

# SolutionA: 74

def input01(full: bool) -> list[str]:
    return readLines(getPath(1, full))

def day01A():
    full = True
    for line in input01(full):
        level = 0
        for x in line:
            if x == '(':
                level += 1
            elif x == ')':
                level -= 1 
        print(level)

if __name__ == '__main__':
    day01A()