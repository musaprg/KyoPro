def main():
    while True:
        buf = input().split()
        if buf[0] == "#":
            return
        g = buf[0]
        y,m,d = map(int,buf[1::])
        y = int(y)
        m = int(m)
        d = int(d)
        if y > 31 or (y == 31 and m >= 5):
            g = "?"
            y -= 30
        print(g,y,m,d)

if __name__ == '__main__':
    main()
