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
    A = list(map(int, input().split()))
    num_turn = 0
    suma = 0
    sumb = 0
    # c_a = 0
    # c_b = N-1
    threshold = 0
    while len(A) != 0:
        total = 0
        if num_turn % 2 == 0: # alice turn
            while len(A) != 0:
                if total > threshold:
                    threshold = total
                    break
                total += A.pop(0)
            suma += total
        else: # bob turn
            while len(A) != 0:
                if total > threshold:
                    threshold = total
                    break
                total += A.pop(-1)
            sumb += total
        num_turn += 1
    print(num_turn, suma, sumb)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        main()
