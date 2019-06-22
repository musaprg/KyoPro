def main():
    N = int(input())
    tasks = [tuple(map(int, input().split())) for _ in range(N)]
    tasks = sorted(tasks, key=lambda x: x[1])
    ct = 0
    for t in tasks:
        if ct+t[0] > t[1]:
            return False
        ct += t[0]
    return True

if __name__ == '__main__':
    if main():
        print("Yes")
    else:
        print("No")
