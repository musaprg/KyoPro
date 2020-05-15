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
    N,M,X = map(int, input().split())
    ca = []
    res = sys.maxsize
    for _ in range(N):
        ca.append(list(map(int, input().split())))
    for i in range(2 ** N):
        tmp = [0]*M
        tmpres = 0
        for j in range(N):
            if ((i >> j) & 1):
                tca = ca[N-1-j]
                tmpres += tca[0]
                for k in range(M):
                    tmp[k] += tca[1+k]
        tassei = True
        for a in tmp:
            if a < X:
                tassei = False
                break
        if tassei:
            res = min(res,tmpres)
    if res != sys.maxsize:
        print(res)
    else:
        print(-1)


if __name__ == '__main__':
    main()
