def select(S, used, i: int):
    ans = 0
    if i == len(S)-1:
        return 0
    if used[s[i]] == None:
        tmp = used.copy()
        tmp[s[i]] = 1
        ans += 1 + select(S, used, i+1)

        
        

def main():
    N = int(input())
    S = input()
    ans = 0
    ans += len(S) # 1文字
    


if __name__ == '__main__':
    print(main() % (10**9+7))
