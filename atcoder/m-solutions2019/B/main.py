def main():
    S = input()
    c = S.count('o')
    l = len(S)
    if c >= 8 or ((15-l)>=(8-c)):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
