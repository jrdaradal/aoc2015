# 2015 Advent of Code Day 06 Solution
# John Roy Daradal

from utils import * 

# SolutionA: 400410
# SolutionB: 15343601

cmd = tuple[int,int,int,int,int] # (1/0/-1), x1, y1, x2, y2
on, off, toggle = 'turn on', 'turn off', 'toggle'

def input06(full: bool, mask: dict[str,int]) -> list[cmd]:
    def convert(line: str) -> cmd:
        if line.startswith(on):
            b = mask[on]
        elif line.startswith(off):
            b = mask[off]
        elif line.startswith(toggle):
            b = mask[toggle]
        p = line.split('through')
        c1 = p[0].split()[-1].strip()
        c2 = p[1].strip()
        x1,y1 = [int(x) for x in c1.split(',')]
        x2,y2 = [int(x) for x in c2.split(',')]
        return (b,x1,y1,x2+1,y2+1)

    return [convert(line) for line in readLines(getPath(6, full))]

def day06A():
    full = True
    mask = {on: 1, off: 0, toggle: -1}
    grid = {(x,y): False for x in range(1000) for y in range(1000)}
    for b,x1,y1,x2,y2 in input06(full, mask):
        for x in range(x1,x2):
            for y in range(y1,y2):
                if b == -1:
                    grid[(x,y)] = not grid[(x,y)]
                else:
                    grid[(x,y)] = bool(b)
    print(sum(grid.values()))

def day06B():
    full = True 
    mask = {on: 1, off: -1, toggle: 2}
    grid = {(x,y): 0 for x in range(1000) for y in range(1000)}
    for b,x1,y1,x2,y2 in input06(full, mask):
        for x in range(x1,x2):
            for y in range(y1,y2):
                value = grid[(x,y)] + b 
                grid[(x,y)] = max(value, 0)
    print(sum(grid.values()))

if __name__ == '__main__':
    # day06A()
    day06B()