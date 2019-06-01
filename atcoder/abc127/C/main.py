def main():
    N,M = map(int, input().split())
    lr = []
    for _ in range(M):
        l,r = map(int, input().split())
        lr.append((l,r))
    lr1 = sorted(lr, key=lambda x: x[0])
    lr2 = sorted(lr, key=lambda x: x[1])
    res = lr2[0][1] - lr1[-1][0] + 1
    if res < 0:
        res = 0
    print(res)

if __name__ == '__main__':
    main()
