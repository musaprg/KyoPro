import sys
def main():
    n = int(input())
    d = ""
    while len(d) != n:
        d += "".join(input().split())
    digits = set()
    for i in range(n):
        for j in range(i+1,n+1):
            # print(i,j)
            seq = d[i:j]
            if not seq:
                continue
            digits.add(int(seq))
    digits = sorted(list(digits))
    for i in range(digits[-1]+1):
        if i != digits[i]:
            print(i)
            return
            

if __name__ == '__main__':
    main()