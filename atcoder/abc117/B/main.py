
def main():
    N = int(input())
    Ls = list(map(int, input().split()))
    Ls.sort()
    if(sum(Ls[0:len(Ls)-1]) > Ls[-1]):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
