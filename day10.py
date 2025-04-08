# 2015 Advent of Code Day 10 Solution
# John Roy Daradal

from utils import * 

# SolutionA: 252594

def input10(full: bool) -> tuple[str,int]:
    lines = readLines(getPath(10, full))
    p = lines[0].split()
    return (p[0], int(p[1]))

def day10A():
    full = True 
    curr, count = input10(full)
    for i in range(count):
        next = []
        d, r = curr[0], 1
        for x in curr[1:]:
            if x == d:
                r += 1
            else:
                next.append(str(r))
                next.append(d)
                d, r = x, 1
        next.append(str(r))
        next.append(d)
        curr = ''.join(next)
    print(len(curr))

if __name__ == '__main__':
    day10A()