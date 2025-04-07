# 2015 Advent of Code Day 05 Solution
# John Roy Daradal

from utils import * 

# SolutionA: 236

def input05(full: bool) -> list[str]:
    return readLines(getPath(5, full))

def day05A():
    full = True 
    count = 0 
    for word in input05(full):
        if isNice(word):
            count += 1
    print('Nice:', count)

invalid = ('ab','cd','pq','xy')
vowels = ('a', 'e', 'i', 'o', 'u')

def isNice(word: str) -> bool:
    if any(x in word for x in invalid):
        return False
    hasRepeat = False 
    count = {}
    prev = word[0]
    count[prev] = 1
    for curr in word[1:]:
        count[curr] = count.get(curr, 0) + 1
        if prev == curr:
            hasRepeat = True
        prev = curr
    if not hasRepeat:
        return False
    numVowels = sum(count.get(v,0) for v in vowels)
    if numVowels < 3:
        return False
    
    return True


if __name__ == '__main__':
    day05A()