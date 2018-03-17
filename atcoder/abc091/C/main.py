import math
import sys
from pprint import pprint

def distance(a,b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def solve(reds, blues):
    ans = []
    while len(blues) != 0:
        blue = blues.pop(0)
        # print("-----")
        # pprint(reds)
        # pprint(blues)
        red_ans = reds[0]
        min_d = sys.maxsize
        # skip_f = False
        for red in reds:
            if blue[0] > red[0] and blue[1] > red[1] and (red, blue) not in ans:
                d = distance(red, blue)
                if min_d > d:
                    red_ans = red
                    min_d = d
        if min_d != sys.maxsize:
            # print("{} <-> {}".format(red_ans, blue))
            ans.append((red_ans, blue))
            reds.remove(red_ans)
    # pprint(reds)
    # pprint(blues)
    # while len(reds) != 0:
    #     red = reds.pop()
    #     # print("-----")
    #     # pprint(reds)
    #     # pprint(blues)
    #     blue_ans = blues[0]
    #     min_d = sys.maxsize
    #     for blue in blues:
    #         if blue[0] > red[0] and blue[1] > red[1] and (red, blue) not in ans:
    #             d = distance(red, blue)
    #             if min_d > d:
    #                 blue_ans = blue
    #                 min_d = d
    #     if min_d != sys.maxsize:
    #         # print("{} <-> {}".format(red, blue_ans))
    #         ans.append((red, blue_ans))
    #         blues.remove(blue_ans)
    # pprint(ans)
    return len(ans)

if __name__ == '__main__':
    N = int(input())
    reds = []
    for i in range(N):
        a,b = list(map(lambda x: int(x), input().split(" ")))
        reds.append((a,b))
    blues = []
    for i in range(N):
        c,d = list(map(lambda x: int(x), input().split(" ")))
        blues.append((c,d))
    ans = []
    reds.sort()
    blues.sort()
    ans = solve(reds, blues)
    print(ans)