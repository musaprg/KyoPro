import sys
from collections import defaultdict, Counter, deque
from itertools import accumulate, permutations, combinations
from operator import itemgetter
from bisect import bisect_left, bisect_right, bisect
from heapq import heappop, heappush
from fractions import gcd
from math import ceil, floor, sqrt, cos, sin, pi
from copy import deepcopy

# If you use recursive call, uncomment this code
#sys.setrecursionlimit(10**6)

def visualize(me,target):
    #print("me @ ({},{})".format(me[0],me[1]))
    print("target @ ({},{})".format(target[0],target[1]))
    #for x,y in range(target[0],target[1]):
    #    if x == me[0] and y == me[1]:
    #        print("■")

def distance(a):
    return abs(a[0]) + abs(a[1])

def solve():
    X,Y,S = input().split()
    target = [int(X), int(Y)]
    me = [0]*2
    c = Counter(S)
    time = 0
    for s in S:
        #visualize(me,target)
        dx,dy = 0,0
        if s == "N":
            dy = 1
        elif s == "S":
            dy = -1
        elif s == "W":
            dx = -1
        else:
            dx = 1
        target[0] += dx
        target[1] += dy
        time += 1
        if distance(target) <= time:
            return time
    return "IMPOSSIBLE"


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        print("Case #{0}: {1}".format(i+1, solve()))
