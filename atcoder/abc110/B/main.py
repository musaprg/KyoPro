def main():
    N, M, X, Y = map(int, input().split())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))

    xs = sorted(xs)
    ys = sorted(ys)

    print(xs)
    print(ys)

    count = ys[0] - xs[-1]
    
    for i in range(count):
        Z = xs[-1] + i + 1
        if X < Z and Z <= Y:
            return False

    return True


if __name__ == '__main__':
    if main():
        print("War")
    else:
        print("No War")