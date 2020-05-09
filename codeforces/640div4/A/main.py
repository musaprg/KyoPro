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
    N = int(input())
    for _ in range(N):
        res = []
        n = input()
        n = n[::-1]
        dd = 1
        for i in range(len(n)):
            if n[i] == "0":
                continue
            res.append(str(int(n[i]) * (10**i)))
        print(len(res))
        print(" ".join(res))

if __name__ == '__main__':
    main()
