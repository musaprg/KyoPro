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
    H,W,K = map(int, input().split())
    C = []
    for _ in range(H):
        S = input()
        cc = []
        for s in S:
            cc.append(1 if s == "#" else 0)
        C.append(cc)
    ans = 0
    for h in range(1<<H):
        for w in range(1<<W):
            tmp = 0
            for kh in range(H):
                if h>>kh & 1:
                    for kw in range(W):
                        if w>>kw & 1:
                            tmp += C[kh][kw]
            if tmp == K:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
