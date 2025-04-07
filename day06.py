# 2015 Advent of Code Day 06 Solution
# John Roy Daradal

from utils import * 

# SolutionA: 400410
# 

cmd = tuple[int,int,int,int,int] # (1/0/-1), x1, y1, x2, y2

def input06(full: bool) -> list[cmd]:
    def convert(line: str) -> cmd:
        if line.startswith('turn on'):
            b = 1
        elif line.startswith('turn off'):
            b = 0
        elif line.startswith('toggle'):
            b = -1
        p = line.split('through')
        c1 = p[0].split()[-1].strip()
        c2 = p[1].strip()
        x1,y1 = [int(x) for x in c1.split(',')]
        x2,y2 = [int(x) for x in c2.split(',')]
        return (b,x1,y1,x2+1,y2+1)

    return [convert(line) for line in readLines(getPath(6, full))]

def day06A():
    full = True
    grid = {(x,y): False for x in range(1000) for y in range(1000)}
    for b,x1,y1,x2,y2 in input06(full):
        for x in range(x1,x2):
            for y in range(y1,y2):
                if b == -1:
                    grid[(x,y)] = not grid[(x,y)]
                else:
                    grid[(x,y)] = bool(b)
    print(sum(grid.values()))

if __name__ == '__main__':
    day06A()