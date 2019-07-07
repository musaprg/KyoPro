from collections import defaultdict
import sys
import copy

def main():
    flag = False
    while True:
        t = int(input())
        if not t:
            return
        if flag:
            print()
        flag = True
        cclist = (10,50,100,500)
        cc = list(map(int,input().split())) # 10 50 100 500
        csum = sum([c*n for c,n in zip(cclist,cc)])
        ots = otsuri(csum-t)
        for c,n1,n2 in zip(cclist, cc, ots):
            n = n1-n2
            if n <= 0:
                continue
            print(c,n)



def otsuri(n: int):
    res = [0]*4
    l = len(res)-1
    for i,c in enumerate([500,100,50,10]):
        res[l-i] = n // c
        n %= c
    return res


if __name__ == '__main__':
    main()