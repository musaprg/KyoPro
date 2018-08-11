round = lambda x: (x*2+1)//2

def rec(num):
    ans = round(num / (-2))
    remain = num - (-2)*ans
    if ans == 0:
        print(int(remain), end='')
        return
    rec(ans)
    print(int(remain), end='')
    return

def p_ans(num):
    rec(num)
    print()

if __name__ == '__main__':
    N = int(input())
    p_ans(N)



