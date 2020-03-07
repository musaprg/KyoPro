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
    Q = int(input())
    head = ""
    tail = ""
    is_vert_normal = True
    for _ in range(Q):
        query = input().split()
        T = int(query[0])
        if T == 1:
            is_vert_normal = not is_vert_normal
        else:
            F = int(query[1])
            C = query[2]
            if F == 1:
                if is_vert_normal:
                    head += C
                else:
                    tail += C
            else:
                if not is_vert_normal:
                    head += C
                else:
                    tail += C
    if is_vert_normal:
        print(head[::-1] + S + tail)
    else:
        print(tail[::-1] + S[::-1] + head)

if __name__ == '__main__':
    main()
