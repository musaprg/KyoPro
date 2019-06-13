def main():
    while True:
        n,m,p = map(int,input().split())
        if (n,m,p) == (0,0,0):
            return
        ps = [int(input()) for _ in range(n)]
        pool = sum(ps) * 100
        pool = pool * (100-p) // 100 
        if ps[m-1] == 0:
            print(0)
        else:
            print(pool // ps[m-1])

if __name__ == '__main__':
    main()
