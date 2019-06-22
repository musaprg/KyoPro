def main():
    a,b,c,d = map(int, input().split())
    ans = b-a+1
    cd = c*d
    g = gcd(c,d)
    if g != 0:
        cd //= g
    ans -= b//c-(a-1)//c
    ans -= b//d-(a-1)//d
    ans += b//cd-(a-1)//cd
    print(ans)

def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

if __name__ == '__main__':
    main()
