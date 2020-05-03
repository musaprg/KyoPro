import sys
from collections import defaultdict, Counter, deque
from itertools import accumulate, permutations, combinations
from operator import itemgetter
from bisect import bisect_left, bisect_right, bisect
from heapq import heappop, heappush
from fractions import gcd
from math import ceil, floor, sqrt, cos, sin, pi
from copy import deepcopy

from enum import Enum

# If you use recursive call, uncomment this code
#sys.setrecursionlimit(10**6)

def solve():
    S = input()
    num_incomplete_pairs = 0
    num_pairs = 0
    ans = ""
    stack = []
    stack.append(S[0])
    for s in S:
        if len(stack) == 0:
            stack.append(s) 
            ans += "("
            ans += s
            continue
        t = stack.pop()
        if s != t:
            stack.append(s) 
        ans += s

    return ans

def main():
    T = int(input())
    for i in range(1,T+1):
        print("Case #%d: %s", i, solve())

if __name__ == '__main__':
    main()
