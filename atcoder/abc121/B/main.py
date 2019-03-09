def main():
    N,M,C = map(int, input().split())
    B = list(map(int, input().split()))
    count = 0
    for i in range(N):
        A = list(map(int, input().split()))
        ans = C
        for a,b in zip(A,B):
            ans += a * b
        if ans > 0:
            count += 1
    print(count) 

if __name__ == '__main__':
    main()
