def main():
    n = int(input())
    uu = [input() for _ in range(n)]
    m = int(input())
    is_closed = True
    for _ in range(m):
        t = input()
        if t in uu:
            if is_closed:
                print("Opened by", t)
            else:
                print("Closed by", t)
            is_closed = not is_closed
        else:
            print("Unknown", t)


if __name__ == '__main__':
    main()
