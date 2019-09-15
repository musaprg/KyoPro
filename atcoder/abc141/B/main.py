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
    ss = input()
    odd = ["R","U","D"]
    even = ["L","U","D"]
    for s in ss[::2]:
        if not s in odd:
            return False
    for s in ss[1::2]:
        if not s in even:
            return False
    return True

if __name__ == '__main__':
    if main():
        print("Yes")
    else:
        print("No")
