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
S = None
T = None

def main():
    global G, S, T
    N,M = map(int, input().split())
    G = [[0]*N for _ in range(N)]
    for _ in range(M):
        u,v = map(int,input().split())
        G[u][v] = 1
    S,T = map(int,input().split())
    bfs(G, S, T)

def bfs(G, S, T):
    q = deque([S])

    while q:
        v = q.pop()


if __name__ == '__main__':
    main()
