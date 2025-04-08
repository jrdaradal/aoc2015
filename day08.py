# 2015 Advent of Code Day 08 Solution
# John Roy Daradal

import re
from utils import * 

# SolutionA: 1350

def input08(full: bool) -> list[str]:
    return readLines(getPath(8, full))

def day08A():
    full = True 
    total = 0 
    for text in input08(full):
        chars = len(parseString(text))
        total += len(text) - chars 
    print('Total:', total)

def parseString(text: str) -> str:
    text = text[1:-1]
    hex = r'\\x[0-9a-f]{2}'
    text = re.sub(hex, '.', text)
    text = text.replace('\\"', '"')
    text = text.replace('\\\\', '.')
    return text

if __name__ == '__main__':
    day08A()