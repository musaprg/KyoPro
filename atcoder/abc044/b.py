from collections import Counter

def main(s):
    cnt = Counter(s)
    for w, c in cnt.most_common():
        if c%2!=0:
            return "No"
    return "Yes"


if __name__ == '__main__':
    print(main(input()))
