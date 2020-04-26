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
    K = int(input())
    ans = 0
    # a,a,a
    ans += sum(range(1,K+1))

    # a,b,b
    tmp = 0
    memo = defaultdict(int)
    for a in range(1,K+1):
        for b in range(a+1,K+1):
            memo[(a,b)] = memo[(b,a)] = gcd(a,b)
            tmp += memo[(a,b)]
    ans += tmp * 6

    # a,b,c
    tmp = 0
    for a in range(1,K+1):
        for b in range(a+1,K+1):
            for c in range(b+1,K+1):
                ab = memo[(a,b)] if memo[(a,b)] else gcd(a,b)
                memo[(a,b)] = memo[(b,a)] = ab
                abc = memo[(ab,c)] if memo[(ab,c)] else gcd(ab,c)
                memo[(ab,c)] = memo[(c,ab)] = abc
                tmp += abc
    ans += tmp * 6

    print(ans)


if __name__ == '__main__':
    main()
