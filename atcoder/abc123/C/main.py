import math
import sys

def calc(i,r,caps):
    if i == len(caps):
        return 0
    ans = 0
    if caps[i] >= caps[i-1]:
        ans += 1 + calc(i+1,0,caps)
    else:
        ans += 
    

def main():
    N = int(input())
    caps = [int(input()) for _ in range(5)]
    ans = 0
    n = N
    n_r = 0

    for c in caps:
        if c >= n and c >= n_r:
            ans += 1
            continue
        if ans == 0:
            ans = 1
        ans = math.ceil(n/c) + math.ceil(n_r/c)
        n = c
        n_r = n%c

    print(ans)


if __name__ == '__main__':
    main()
