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
    B = list(map(int,input().split()))
    A = [B[0]]
    ans = B[0]
    for i in range(1,N-1):
        tmp = min(B[i-1],B[i])
        ans += tmp
        A.append(tmp)
    tmp = max(A[-1],B[-1])
    A.append(tmp)
    ans += tmp
    #print(A)
    print(ans)

if __name__ == '__main__':
    main()


