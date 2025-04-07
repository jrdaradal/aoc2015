# 2015 Advent of Code Day 02 Solution
# John Roy Daradal 

from utils import * 

# SolutionA: 1606483
# SolutionB: 3842356

dims = tuple[int,int,int]

def input02(full: bool) -> list[dims]:
    lines = readLines(getPath(2, full))
    lines = [tuple(int(x) for x in line.split('x')) for line in lines]
    return lines 

def day02A():
    full = True
    total = 0 
    for l,w,h in input02(full):
        lw, wh, lh = l*w, w*h, l*h 
        total += (2*lw) + (2*wh) + (2*lh) + min(lw,wh,lh)
    print('Total:', total)

def day02B():
    full = True 
    total = 0 
    for d in input02(full):
        d1, d2, d3 = sorted(d)
        total += (2 * (d1+d2)) + (d1*d2*d3) 
    print('Total:', total)

if __name__ == '__main__':
    # day02A()
    day02B()