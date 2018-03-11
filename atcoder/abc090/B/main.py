def is_palindrome(n):
    n = str(n)
    return n[0:len(n)//2+1]==n[::-1][0:len(n)//2+1]

if __name__ == '__main__':
    a,b = list(map(lambda x: int(x), input().split(" ")))
    
    c = 0
    for i in range(a,b+1):
        if is_palindrome(i):
            c += 1
    
    print(c)