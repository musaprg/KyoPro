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
    T = input()
    result = []
    bef = ""
    for i in range(len(T)-1):
        if T[i] == "?":
            if bef == "P":
                result.append("D")
            elif T[i+1] == "?" or T[i+1] == "D":
                result.append("P")
            else:
                result.append("D")
        else:
            result.append(T[i])
        bef = result[-1]
    if T[-1] == "?":
        result.append("D")
    else:
        result.append(T[-1])
    print("".join(result))

if __name__ == '__main__':
    main()
