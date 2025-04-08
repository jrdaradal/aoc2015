# 2015 Advent of Code Day 01 Solution
# John Roy Daradal 

from utils import *

# SolutionA: 74
# SolutionB: 1795

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

def day01B():
    full = True 
    for line in input01(full):
        level = 0 
        for i,x in enumerate(line):
            if x == '(':
                level += 1 
            elif x == ')':
                level -= 1
            if level == -1:
                print(i+1)
                break

if __name__ == '__main__':
    day01A()
    day01B()