def main():
    while True:
        n = int(input())
        if not n:
            return
        aa = list(map(int,input().split()))
        ave = sum(aa)/n
        print(len([x for x in aa if x <= ave]))

if __name__ == '__main__':
    main()
