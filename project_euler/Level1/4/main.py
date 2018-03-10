# 3 x 3 palindrome


def is_palindrome(n):
    n = str(n)
    return n[0:len(n)//2+1] == n[::-1][0:len(n)//2+1]

if __name__ == '__main__':
    ans = 0

    for a in range(0,1000):
        for b in range(0,1000):
            c = a * b
            if ans >= c:
                continue
            if is_palindrome(c):
                ans = c

    print(ans)

