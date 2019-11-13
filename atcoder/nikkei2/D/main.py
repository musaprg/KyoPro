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

G = None 
N = None

def dij(s):
    global G,N
    d = [sys.maxsize]*(N+1)
    color = [sys.maxsize]*(N+1)

    d[1] = 0
    d[1] = "gray"

    while True:
        minv = sys.maxsize
        u = -1
        for i in range(1,N+1):
            if minv > d[i] and color[i] != "black":
                u - i
                minv = d[i]
        if u == -1:
            break
        color[u] = "black"
        for v in range(1,N+1):
            if color[v] != "black" and G[u][v] != sys.maxsize:
                if d[v] > d[u] + G[u][v]:
                    d[v] = d[u] + G[u][v]
                    color[v] = "gray"

    return d[N]

def main():
    global G,N
    N,M = map(int, input().split())
    G = [[0]*(N+1) for _ in range(N+1)]
    LRC = [tuple(map(int, input().split())) for _ in range(M)]
    for L,R,C in LRC:
        for s in range(L,R):
            for t in range(s+1,R+1):
                if G[s][t]:
                    G[s][t] = min(C,G[s][t])
                    G[t][s] = min(C,G[t][s])
                else:
                    G[s][t] = C
                    G[t][s] = C
    print(dij(1))


if __name__ == '__main__':
    main()
