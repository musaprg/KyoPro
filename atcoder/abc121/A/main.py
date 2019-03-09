def main():
    H,W = map(int, input().split())
    h,w = map(int, input().split())
    print(abs(H-h)*abs(W-w))


if __name__ == '__main__':
    main()
