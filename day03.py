# 2015 Advent of Code Day 03 Solution
# John Roy Daradal

from utils import * 

# SolutionA: 2081
# SolutionB: 2341

coords = tuple[int,int] # row,col 

def input03(full: bool) -> list[list[coords]]:
    def convert(line: str) -> list[coords]:
        move: list[coords] = []
        for a in line:
            if a == '>':
                d = (0,1)
            elif a == '<':
                d = (0,-1)
            elif a == '^':
                d = (1,0)
            elif a == 'v':
                d = (-1,0)
            move.append(d)
        return move
    return [convert(line) for line in readLines(getPath(3, full))]

def day03A():
    full = True 
    for moves in input03(full):
        curr = (0,0)
        visited = set([curr])
        for d in moves:
            curr = move(curr, d)
            visited.add(curr)
        print(len(visited))

def day03B():
    full = True 
    for moves in input03(full):
        santa, robo = (0,0), (0,0)
        visited = set([santa])
        numMoves = len(moves)
        for i in range(0, numMoves-1, 2):
            santa = move(santa, moves[i])
            robo = move(robo, moves[i+1])
            visited.add(santa)
            visited.add(robo)
        print('Visited', len(visited))


def move(curr: coords, d: coords) -> coords:
    dy, dx = d 
    y, x = curr 
    return (y+dy, x+dx) 
    
        

if __name__ == '__main__':
    # day03A()
    day03B()
