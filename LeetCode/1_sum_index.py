def myfun(nums, target):
    for i in nums:
        for j in nums:
            if (i + j == target):
                return [nums.index(i), nums.index(j)]
    return []

nums = list(map(int, input().split()))
target = int(input())
print(myfun(nums, target))




