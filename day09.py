# 2015 Advent of Code Day 09 Solution
# John Roy Daradal

import itertools
from utils import * 

# SolutionA: 117
# SolutionB: 909

edgeMap = dict[tuple[str,str],int]

class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges: edgeMap = {}

def input09(full: bool) -> Graph:
    g = Graph()
    for line in readLines(getPath(9, full)):
        p = [x.strip() for x in line.split('=')]
        w = int(p[1])
        v = [x.strip() for x in p[0].split('to')]
        v1,v2 = v 
        g.vertices.add(v1)
        g.vertices.add(v2)
        g.edges[(v1,v2)] = w 
        g.edges[(v2,v1)] = w
    return g 

def day09A():
    full = True
    g = input09(full)
    minDistance = float('inf')
    for path in itertools.permutations(g.vertices):
        minDistance = min(minDistance, computeDistance(path, g.edges))
    print('MinDist:', minDistance)

def day09B():
    full = True
    g = input09(full)
    maxDistance = 0
    for path in itertools.permutations(g.vertices):
        maxDistance = max(maxDistance, computeDistance(path, g.edges))
    print('MaxDist:', maxDistance)


def computeDistance(path: tuple, edges: edgeMap) -> int:
    total = 0
    for i in range(1, len(path)):
        key = (path[i-1], path[i])
        total += edges[key]
    return total

if __name__ == '__main__':
    # day09A()
    day09B()