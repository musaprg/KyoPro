def main():
    N = int(input())
    S = input()
    n = 0b10000
    ans = 0
    for s in S:
        print("{0:0100b}".format(n))
        n<<=1
        if s == "#":
            n += 0b1
        if n & 0b11 == 0b10:
            ans += 1
            n = n&0b00|0b01
    print(ans)


if __name__ == '__main__':
    main()
