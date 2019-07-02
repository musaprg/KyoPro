def main():
    while True:
        a,b = map(int,input().split())
        if not a and not b:
            return
        print(a*b)

if __name__ == '__main__':
    main()