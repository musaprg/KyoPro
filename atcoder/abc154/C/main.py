from collections import defaultdict

def main():
    memo = defaultdict(int)
    N = int(input())
    nums = list(map(int,input().split()))

    for n in nums:
#        print(n)
        if memo[n]:
            return False
        else:
            memo[n] += 1
    return True

if __name__ == '__main__':
    if main():
        print("YES")
    else:
        print("NO")
