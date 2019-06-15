from pprint import pprint
from collections import defaultdict
from operator import sub

def main():
    N = int(input())
    balls = [tuple(map(int,input().split())) for _ in range(N)]
    d = defaultdict(int)
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            d[tuple(map(sub, balls[i], balls[j]))] += 1
    try:
        # ！！！！！！！！！！アホ丸出し回避重要ポイント！！！！！！！！！！！！！！
        # maxはEmptyなものに対して実行するとValueErrorを返す
        # 必ずdefaultオプションを付加すること。
        # この仕様理解してないせいで33REしたアホなので利根川に飛び込みます
        # † https://atcoder.jp/contests/diverta2019-2/submissions?f.User=musaprg †
        # ！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        mmax = N- max(d.values(), default=0)
        print(mmax)
    except RuntimeError:
        print(100)


if __name__ == '__main__':
    main()
