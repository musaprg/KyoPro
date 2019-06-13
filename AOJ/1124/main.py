def main():
    while True:
        n,q = map(int,input().split())
        if not n and not q:
            return
        res = [0 for _ in range(1000)]
        for _ in range(n):
            for m in list(map(int,input().split()))[1::]:
                res[m] += 1
        ans = max(res)
        if ans < q:
            print(0)
        else:
            print(res.index(ans))

if __name__ == '__main__':
    main()

