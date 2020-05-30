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
    N,M = map(int,input().split())
    shirube = [None]*(N+1)
    shirube[1] = (1,0)
    mmap = [[] for _ in range(N+1)]
    for _ in range(M):
        a,b = map(int,input().split())
        mmap[a].append(b)
        mmap[b].append(a)
    queue = deque()
    queue.appendleft((1,0))
    while queue:
        current_node, distance = queue.pop()
        for next_node in mmap[current_node]:
            new_distance = distance+1
            if shirube[next_node] is None:
                shirube[next_node] = (current_node, new_distance)
                queue.appendleft((next_node, new_distance))
            elif shirube[next_node][1] > new_distance:
                shirube[next_node] = (current_node, new_distance)
                queue.appendleft((next_node, new_distance))
    shirube = shirube[1::]
    if None in shirube:
        print("No")
        return
    print("Yes")
    for s in shirube[1::]:
        print(s[0])


if __name__ == '__main__':
    main()
