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
    s = [[1 if x == "#" else 0 for x in input()] for _ in range(5)]
    c = 1
    threshold = 4*N
    ans = ""
    while c < threshold:
        cend = c+4
        if sum(s[0][c:cend]) == 1:
            ans += "1"
        elif sum(s[0][c:cend]) == 2:
            ans += "4"
        elif sum(s[1][c:cend]) == 1: # 2 or 3 or 6 or 7
            if s[1][c]:
                if s[3][c]:
                    ans += "6"
                else:
                    ans += "5"
            elif sum(s[2][c:cend]) == 1:
                ans += "7"
            elif s[3][c]:
                ans += "2"
            else:
                ans += "3"
        elif sum(s[2][c:cend]) == 2: # 0 or 8 or 9
            ans += "0"
        elif sum(s[3][c:cend]) == 1:
            ans += "9"
        else:
            ans += "8"
        c += 4
    print(ans)
            


if __name__ == '__main__':
    main()
