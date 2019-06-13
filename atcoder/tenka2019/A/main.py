def main():
    num = list(map(int, input().split()))
    hoge = num[0:2]
    hoge.sort()
    if hoge[0]<=num[2] and num[2]<=hoge[1]:
      print("Yes")
    else:
      print("No")

if __name__ == '__main__':
    main()
