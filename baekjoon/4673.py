nums = set(range(1,10000))
removeNums = set()
for i in nums:
    for j in str(i):
        i += int(j)
    removeNums.add(i)
nums = nums - removeNums
for i in sorted(nums):
    print(i)