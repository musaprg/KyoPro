nums = list(map(int, input().split()))
nums = sorted(nums)
nums.reverse()
print(nums[0]*10+nums[1] + nums[2])