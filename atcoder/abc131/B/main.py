import sys

def main():
    N,L = map(int, input().split())
    apples = [L+i-1 for i in range(1,N+1)]
    mmin = sys.maxsize
    allsum = sum(apples)
    ans = 0
    for i in range(N):
        tmpsum = sum(apples[:i])
        if i != N-1:
            tmpsum += sum(apples[i+1:])
        tmp = abs(allsum-tmpsum)
        if tmp < mmin:
            mmin = tmp
            ans = tmpsum
    print(ans)

if __name__ == '__main__':
    main()
