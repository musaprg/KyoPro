from pprint import pprint

def main():
    N,D = map(int,input().split())
    a,D = calcabc(D,2)
    b,D = calcabc(D,3)
    c,D = calcabc(D,5)
    if D > 1:
        return 0
    dp = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]

    dp[0][0][0] = 1           # 2^a*3^b*5^c

    for n in range(1,N+1):
        tmp = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
        for i in range(0,min(n,a)+1):
            for j in range(0, min(n-i,b)+1):
                for k in range(0, min(n-i-j,c)+1):
                    tmp[i][j][k] = dp[i][j][k]
                    tmp[i][j][k] += dp[i-1][j][k] * 1/6
                    tmp[i][j][k] += dp[i][j-1][k] * 1/6
                    tmp[i][j][k] += dp[i-2][j][k] * 1/6
                    tmp[i][j][k] += dp[i][j][k-1] * 1/6
                    tmp[i][j][k] += dp[i-1][j-1][k] * 1/6
        dp = tmp

    pprint(dp)

    return dp[a][b][c]

def calcabc(n,k):
    ans = 0
    while n%k == 0:
        ans += 1
        n /= k
    return ans, n

if __name__ == '__main__':
    print(main())
