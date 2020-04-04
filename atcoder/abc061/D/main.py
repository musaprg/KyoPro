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
    global N,M,edge,d,prev
    N,M = map(int, input().split())
    edge = defaultdict(lambda: defaultdict(lambda: int(sys.maxsize)))
    d = [sys.maxsize]*N
    prev = [-1]*N
    for _ in range(M):
        a,b,c = map(int, input().split())
        edge[a-1][b-1] = -1 * c
    
    # Bellman-Ford
    if not bellmanford(): # detect inf candidates
        if check_cyclic():
            return "inf"

    return d[N-1]

def check_cyclic():
    global N,M,edge,d,prev
    nodes = set()
    t = N-1
    while True:
        nt = prev[t]
        if nt in nodes:
            return True
        elif nt == -1:
            return False
        nodes.add(nt)
        t = nt

def bellmanford():
    global N,M,edge,d,prev
    d[0] = 0
    for i in range(N):
        for v in range(N):
            for k in range(N):
                if edge[v][k] != sys.maxsize:
                    if d[v] != sys.maxsize and d[i] > d[v] + edge[v][i]:
                        d[i] = d[v] + edge[v][i]
                        prev[i] = v
                        if i == N-1: return True

if __name__ == '__main__':
    print(main())
