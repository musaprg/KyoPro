import re

def get_substrs(s):
    strs = set()
    l = len(s)
    for i in range(l):
        for k in range(i,l):
            strs.add(s[i:k+1])
    return strs

if __name__ == '__main__':
    s = input()
    K = int(input())
    strs = get_substrs(s)
    strs = list(strs)
    strs.sort()
    print(strs[K-1])