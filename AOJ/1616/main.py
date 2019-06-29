def main():
    while True:
        n,m = map(int,input().split())
        if not n and not m:
            return
        aa = list(map(int,input().split()))
        ans = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                tmp = aa[i] + aa[j]
                if tmp <= m:
                    ans = max(ans, tmp)
        if ans == 0:
            print("NONE")
        else:
            print(ans)

if __name__ == '__main__':
    main()
