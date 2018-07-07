if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        a = list(map(int, input().split()))
        a.sort()
        print(a[-1])
