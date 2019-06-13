def main():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    BC = [tuple(map(int, input().split())) for _ in range(M)]
    for b,c in BC:
        print(A)
        for i in range(N):
            if b == 0:
                break
            if A[i] < c:
                A[i] = c
                b -= 1
    print(sum(A))

if __name__ == '__main__':
    main()
