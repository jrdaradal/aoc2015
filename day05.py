# 2015 Advent of Code Day 05 Solution
# John Roy Daradal

from utils import * 

# SolutionA: 236
# SolutionB: 51

def input05(full: bool) -> list[str]:
    return readLines(getPath(5, full))

def day05A():
    full = True 
    count = 0 
    for word in input05(full):
        if isNice(word):
            count += 1
    print('Nice:', count)

def day05B():
    full = True 
    count = 0 
    for word in input05(full):
        if isNiceV2(word):
            count +=1 
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

def isNiceV2(word: str) -> bool:
    numLetters = len(word)
    hasRepeat = False 
    for i in range(2, numLetters):
        if word[i] == word[i-2]:
            hasRepeat = True 
            break
    if not hasRepeat:
        return False 
    pairs = {}
    for i in range(0, numLetters-1):
        pair = word[i:i+2]
        if pair not in pairs:
            pairs[pair] = []
        pairs[pair].append(i)
    hasPair = False 
    for pair,indexes in pairs.items():
        if len(indexes) == 2:
            idx1, idx2 = indexes 
            if abs(idx1-idx2) > 1:
                hasPair = True 
                break
        elif len(indexes) >= 3:
            hasPair = True 
            break
    if not hasPair:
        return False
    
    return True

if __name__ == '__main__':
    # day05A()
    day05B()