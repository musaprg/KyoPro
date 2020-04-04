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
    S = input()
    if len(S)%2!=0:
        return "No"
    for i in range(len(S)//2):
        t = i*2
        if S[t:t+2] != "hi":
            return "No"
    return "Yes"

if __name__ == '__main__':
    print(main())
