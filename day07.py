# 2015 Advent of Code Day 07 Solution
# John Roy Daradal

from utils import * 

# SolutionA: 3176
# SolutionB: 14710

LET, AND, OR, NOT, LSHIFT, RSHIFT = 'LET', 'AND', 'OR', 'NOT', 'LSHIFT', 'RSHIFT'

def input07(full: bool) -> list[tuple]:
    def convert(line: str) -> tuple:
        p = [x.strip() for x in line.split('->')]
        expr, res = p[0], p[1]
        if AND in expr:
            v0, v1 = [tryParseInt(x.strip()) for x in expr.split(AND)]
            return (res, AND, v0, v1)
        elif OR in expr:
            v0, v1 = [tryParseInt(x.strip()) for x in expr.split(OR)]
            return (res, OR, v0, v1)
        elif LSHIFT in expr:
            v0, v1 = [tryParseInt(x.strip()) for x in expr.split(LSHIFT)]
            return (res, LSHIFT, v0, v1)
        elif RSHIFT in expr:
            v0, v1 = [tryParseInt(x.strip()) for x in expr.split(RSHIFT)]
            return (res, RSHIFT, v0, v1)
        elif NOT in expr:
            v = expr.split(NOT)[-1].strip()
            return (res, NOT, v)
        else:
            v = tryParseInt(expr)
            return (res, LET, v)
    return [convert(line) for line in readLines(getPath(7, full))]

def day07A():
    full = True 
    solveA(full)

def day07B():
    full = True 
    override = {'b': 3176}
    solveA(full, override)

def solveA(full: bool, override: dict[str,int]|None = None):
    value = {}
    defer = []
    for cmd in input07(full):
        rcv, op = cmd[0], cmd[1]
        if op == LET:
            v = cmd[2]
            if type(v) == int:
                value[rcv] = v
            else:
                defer.append(([v], rcv, op, None))
        elif op == AND or op == OR:
            vars, consts = getVars([cmd[2], cmd[3]])
            defer.append((vars, rcv, op, consts[0] if len(consts) > 0 else None))
        elif op == LSHIFT or op == RSHIFT:
            defer.append(([cmd[2]], rcv, op, cmd[3]))
        elif op == NOT:
            defer.append(([cmd[2]], rcv, op, None))

    if override is not None:
        for k,v in override.items():
            value[k] = v

    while len(defer) > 0:
        defer2 = []
        for d in defer:
            x, rcv, op, param = d
            if any(v not in value for v in x):
                defer2.append(d)
                continue
            if op == AND:
                value[rcv] = value[x[0]] & (value[x[1]] if param is None else param)
            elif op == OR:
                value[rcv] = value[x[0]] | (value[x[1]] if param is None else param)
            elif op == LSHIFT:
                value[rcv] = value[x[0]] << param
            elif op == RSHIFT:
                value[rcv] = value[x[0]] >> param
            elif op == NOT:
                value[rcv] = ~value[x[0]]
            elif op == LET:
                value[rcv] = value[x[0]]
            if value[rcv] < 0:
                value[rcv] += 65536
        defer = defer2
        if 'a' in value:
            break
    print(value['a'])

def tryParseInt(x: str) -> int|str:
    return int(x) if x.isdecimal() else x

def getVars(items: list) -> tuple[list, list]:
    vars = [x for x in items if type(x) == str]
    consts = [x for x in items if type(x) == int]
    return (vars, consts)

if __name__ == '__main__':
    # day07A()
    day07B()