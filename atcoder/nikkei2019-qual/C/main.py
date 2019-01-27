import math
import collections

def solve(N,A,B,AB):
    na = math.ceil(N/2)
    nb = N - na
    print(na)
    print(nb)

    ans = 0

    print(AB)

    for _,ll in AB.items():
        while ll and na > 0:
            ans += ll.pop(0)[0]
            na -= 1
            print(AB)

    print("---")

    for _,ll in AB.items():
        print(AB)
        while ll and nb > 0:
            ans -= B[ll.pop()[1]]
            nb -= 1

    print(AB)

    return ans



def main():
    N = int(input())
    A = []
    B = []
    AB = collections.OrderedDict()
    for i in range(N):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)
        key = str(a-b)
        if not key in AB.keys():
            AB[str(a-b)] = [(a,i)]
        else:
            AB[str(a-b)].append((a,i))
        AB[str(a-b)].sort(key=lambda x: x[0])
        AB[str(a-b)].reverse()

    print(AB)
    print("-------")
    print(solve(N,A,B,AB))


if __name__ == '__main__':
    main()
