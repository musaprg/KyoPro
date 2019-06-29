def main():
    n = int(input())
    count = {"A":0, "Un":0}
    for _ in range(n):
        s = input()
        count[s] += 1
        if count["A"] < count["Un"]:
            return False
    if count["A"] == count["Un"]:
        return True
    else:
        return False

if __name__ == '__main__':
    if main():
        print("YES")
    else:
        print("NO")
