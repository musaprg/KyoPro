import sys
def main():
    while True:
        n = int(input())
        if not n:
            return
        aa = list(map(int,input().split()))
        ans = sys.maxsize
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                ans = min(abs(aa[i]-aa[j]),ans)
        print(ans)


if __name__ == '__main__':
    main()
