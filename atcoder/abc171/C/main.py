import sys
from collections import defaultdict, Counter, deque
from itertools import accumulate, permutations, combinations
from operator import itemgetter
from bisect import bisect_left, bisect_right, bisect
from heapq import heappop, heappush
from fractions import gcd
from math import ceil, floor, sqrt, cos, sin, pi
from copy import deepcopy
from string import ascii_lowercase

# If you use recursive call, uncomment this code
sys.setrecursionlimit(10**6)

count = 0

def main(N):
    answer = ""
    while N > 0:
        N -= 1
        t = N % 26
        answer += chr(ord("a")+t)
        N //= 26
    print(answer[::-1])

if __name__ == '__main__':
    N = int(input())
    #for i in range(1,30):
    #    main(i)    
    main(N)
