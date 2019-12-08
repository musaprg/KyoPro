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

def main():
    s = input()
    t = len(s)//2
    ls = s[:t]
    rs = None
    c = 0
    if len(s)%2==0:
        rs = s[t:]
    else:
        rs = s[t+1:]
    rs = rs[::-1]
    #print(ls,rs)
    for l,r in zip(ls,rs): 
        if l != r:
            c += 1
    print(c)

if __name__ == '__main__':
    main()
