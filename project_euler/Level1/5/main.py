def gcd(a,b):
    while True:
        r = a % b
        if r == 0:
            return b
        a = b
        b = r

def solve_with_range(m,n):
    ans = 1
    for i in range(m,n):
        g = gcd(ans,i)
        if g == 0:
            ans *= i
        else:
            ans *= i//g
    return ans


if __name__ == '__main__':
    #a,b = list(map(lambda x: int(x), input().split(" ")))
    #print(gcd(a,b))
    #print(solve_with_range(a,b))

    ans = solve_with_range(1,20+1)
    print(ans)


