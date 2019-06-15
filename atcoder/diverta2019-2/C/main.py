
def main():
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    res = []
    while len(nums) != 2:
        x = nums.pop(0)
        y = nums.pop(0)
        nums.append(x-y)
        res.append((x,y))
    print(nums[0]-nums[1])
    for r in res:
        print(r[0], r[1])
    print(nums[0], nums[1])
        



if __name__ == '__main__':
    main()
